"""
Azure AD → LiteLLM Proxy Authentication Helper
================================================
Uses the OAuth2 client-credentials flow to obtain an Azure AD access token,
then uses it to call models through a LiteLLM proxy.

Setup:
  1. Copy .env.example → .env
  2. Fill in the AZURE_* and LITELLM_PROXY_URL values
  3. Run:  python azure_litellm_auth.py
"""

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

# ─── Required Environment Variables ───────────────────────────────────────────

REQUIRED_VARS = [
    "AZURE_TENANT_ID",
    "AZURE_CLIENT_ID",
    "AZURE_CLIENT_SECRET",
    "AZURE_SCOPE",
    "LITELLM_PROXY_URL",
]


def check_env():
    """Validate that all required environment variables are set."""
    missing = [v for v in REQUIRED_VARS if not os.getenv(v)]
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f"   • {var}")
        print("\n→ Copy .env.example to .env and fill in your Azure credentials.")
        sys.exit(1)


# ─── Step 1: Fetch Azure AD Token ────────────────────────────────────────────

def get_azure_token() -> str:
    """
    Authenticate with Azure AD using the client-credentials grant.

    Returns:
        str: The access token.
    """
    tenant_id = os.getenv("AZURE_TENANT_ID")
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    response = requests.post(token_url, data={
        "grant_type": "client_credentials",
        "client_id": os.getenv("AZURE_CLIENT_ID"),
        "client_secret": os.getenv("AZURE_CLIENT_SECRET"),
        "scope": os.getenv("AZURE_SCOPE"),
    })

    if response.status_code != 200:
        print(f"❌ Token request failed ({response.status_code}):")
        print(response.json())
        sys.exit(1)

    token = response.json()["access_token"]
    print("✅ Azure AD token acquired!")
    return token


# ─── Step 2: Generate a LiteLLM Virtual Key (Optional) ───────────────────────

def generate_litellm_key(access_token: str, duration: str = "1h") -> str:
    """
    Call the LiteLLM proxy's /key/generate endpoint to get a virtual key.

    Args:
        access_token: Azure AD bearer token.
        duration: How long the key should be valid (e.g., '1h', '24h', '30d').

    Returns:
        str: The generated LiteLLM API key.
    """
    proxy_url = os.getenv("LITELLM_PROXY_URL").rstrip("/")

    response = requests.post(
        f"{proxy_url}/key/generate",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"duration": duration},
    )

    if response.status_code != 200:
        print(f"❌ Key generation failed ({response.status_code}):")
        print(response.json())
        sys.exit(1)

    key = response.json()["key"]
    print(f"✅ LiteLLM key generated (expires in {duration}): {key[:12]}...")
    return key


# ─── Step 3: Test a Chat Completion ──────────────────────────────────────────

def test_completion(api_key: str, model: str = "gpt-4o"):
    """
    Send a test chat completion request through the LiteLLM proxy.

    Args:
        api_key: Either the Azure AD token or a generated LiteLLM key.
        model: The model to test with.
    """
    proxy_url = os.getenv("LITELLM_PROXY_URL").rstrip("/")

    response = requests.post(
        f"{proxy_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": "Say hello in one sentence."}],
            "max_tokens": 50,
        },
    )

    if response.status_code != 200:
        print(f"❌ Completion failed ({response.status_code}):")
        print(response.json())
        return

    reply = response.json()["choices"][0]["message"]["content"]
    print(f"✅ Model ({model}) replied: {reply}")


# ─── Step 4: Using with litellm Python SDK ───────────────────────────────────

def test_with_litellm_sdk(api_key: str, model: str = "gpt-4o"):
    """
    Use the litellm Python SDK instead of raw HTTP requests.

    Args:
        api_key: Either the Azure AD token or a generated LiteLLM key.
        model: The model to test with.
    """
    try:
        import litellm
    except ImportError:
        print("⚠️  litellm not installed. Run: pip install litellm")
        return

    proxy_url = os.getenv("LITELLM_PROXY_URL").rstrip("/")

    response = litellm.completion(
        model=model,
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
        api_base=proxy_url,
        api_key=api_key,
        max_tokens=50,
    )

    reply = response.choices[0].message.content
    print(f"✅ [SDK] Model ({model}) replied: {reply}")


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    check_env()

    # 1. Get Azure AD token
    token = get_azure_token()

    # 2. Option A: Use the token directly as an API key
    print("\n--- Testing with Azure AD token directly ---")
    test_completion(api_key=token)

    # 3. Option B: Generate a short-lived LiteLLM key (uncomment to use)
    # print("\n--- Generating LiteLLM virtual key ---")
    # litellm_key = generate_litellm_key(token, duration="1h")
    # test_completion(api_key=litellm_key)

    # 4. Optional: Test with litellm SDK
    # print("\n--- Testing with litellm SDK ---")
    # test_with_litellm_sdk(api_key=token)
