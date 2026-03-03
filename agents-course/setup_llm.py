"""
setup_llm.py — Shared LLM Configuration for All Notebooks
==========================================================
Import this module in each notebook to get a properly configured litellm
environment. Automatically detects LiteLLM proxy credentials (Azure AD)
and routes all calls through the proxy when available.

Usage:
    from setup_llm import DEFAULT_MODEL, DEFAULT_EMBEDDING, is_proxy_mode
"""

import os
import sys
import requests
from dotenv import load_dotenv
import litellm

# ─── Load Environment ─────────────────────────────────────────────────────────
load_dotenv()

# ─── Configuration ────────────────────────────────────────────────────────────
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
DEFAULT_EMBEDDING = os.getenv("DEFAULT_EMBEDDING_MODEL", "text-embedding-3-small")

# ─── Internal State ───────────────────────────────────────────────────────────
_proxy_active = False
_proxy_token = None


def is_proxy_mode() -> bool:
    """Check if LiteLLM proxy mode is active."""
    return _proxy_active


def _get_azure_token() -> str:
    """Fetch an Azure AD access token using client credentials."""
    tenant_id = os.getenv("AZURE_TENANT_ID")
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    response = requests.post(token_url, data={
        "grant_type": "client_credentials",
        "client_id": os.getenv("AZURE_CLIENT_ID"),
        "client_secret": os.getenv("AZURE_CLIENT_SECRET"),
        "scope": os.getenv("AZURE_SCOPE"),
    })

    if response.status_code != 200:
        print(f"⚠️ Azure AD token request failed ({response.status_code}): {response.text[:200]}")
        return None

    return response.json().get("access_token")


def _configure_proxy():
    """Configure litellm to route through the proxy."""
    global _proxy_active, _proxy_token

    proxy_url = os.getenv("LITELLM_PROXY_URL", "").rstrip("/")
    has_azure_creds = all([
        os.getenv("AZURE_TENANT_ID"),
        os.getenv("AZURE_CLIENT_ID"),
        os.getenv("AZURE_CLIENT_SECRET"),
        os.getenv("AZURE_SCOPE"),
    ])

    if not proxy_url:
        return  # No proxy configured, use direct provider keys

    if has_azure_creds:
        # Fetch Azure AD token
        token = _get_azure_token()
        if token:
            _proxy_token = token
            litellm.api_base = proxy_url
            litellm.api_key = token
            _proxy_active = True
            return

    # Proxy URL set but no Azure creds — try using proxy with existing key
    litellm_key = os.getenv("LITELLM_API_KEY")
    if litellm_key:
        litellm.api_base = proxy_url
        litellm.api_key = litellm_key
        _proxy_active = True


def get_proxy_token() -> str:
    """Get the current proxy token (for use with LangChain, etc.)."""
    return _proxy_token


def get_langchain_llm(model=None, temperature=0):
    """
    Get a LangChain ChatOpenAI instance configured for proxy or direct mode.

    Usage:
        from setup_llm import get_langchain_llm
        llm = get_langchain_llm()
    """
    from langchain_openai import ChatOpenAI

    model = model or DEFAULT_MODEL
    kwargs = {"model": model, "temperature": temperature}

    if _proxy_active:
        proxy_url = os.getenv("LITELLM_PROXY_URL", "").rstrip("/")
        kwargs["openai_api_base"] = proxy_url
        kwargs["openai_api_key"] = _proxy_token or os.getenv("LITELLM_API_KEY", "sk-placeholder")

    return ChatOpenAI(**kwargs)


def get_langchain_embeddings(model=None):
    """
    Get a LangChain OpenAIEmbeddings instance configured for proxy or direct mode.

    Usage:
        from setup_llm import get_langchain_embeddings
        embeddings = get_langchain_embeddings()
    """
    from langchain_openai import OpenAIEmbeddings

    model = model or DEFAULT_EMBEDDING
    kwargs = {"model": model}

    if _proxy_active:
        proxy_url = os.getenv("LITELLM_PROXY_URL", "").rstrip("/")
        kwargs["openai_api_base"] = proxy_url
        kwargs["openai_api_key"] = _proxy_token or os.getenv("LITELLM_API_KEY", "sk-placeholder")

    return OpenAIEmbeddings(**kwargs)


# ─── Auto-configure on import ────────────────────────────────────────────────
_configure_proxy()

# ─── Print Status ─────────────────────────────────────────────────────────────
if _proxy_active:
    proxy_url = os.getenv("LITELLM_PROXY_URL", "")
    print(f"🔗 LiteLLM Proxy Mode: {proxy_url}")
    print(f"   Model: {DEFAULT_MODEL} | Embedding: {DEFAULT_EMBEDDING}")
else:
    providers = {
        "OpenAI": os.getenv("OPENAI_API_KEY"),
        "Google": os.getenv("GOOGLE_API_KEY"),
        "Anthropic": os.getenv("ANTHROPIC_API_KEY"),
    }
    available = [k for k, v in providers.items() if v and not v.startswith("your-")]
    print(f"🔑 Direct Mode — Providers: {', '.join(available) if available else '⚠️ None configured'}")
    print(f"   Model: {DEFAULT_MODEL} | Embedding: {DEFAULT_EMBEDDING}")


# ─── Run standalone to test ───────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n--- Testing setup_llm ---")
    print(f"Proxy active: {is_proxy_mode()}")
    print(f"DEFAULT_MODEL: {DEFAULT_MODEL}")
    print(f"DEFAULT_EMBEDDING: {DEFAULT_EMBEDDING}")

    # Quick smoke test
    try:
        response = litellm.completion(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": "Say 'hello' in one word."}],
            max_tokens=10,
        )
        print(f"✅ Test call succeeded: {response.choices[0].message.content}")
    except Exception as e:
        print(f"❌ Test call failed: {e}")
