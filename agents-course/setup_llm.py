"""
setup_llm.py — Shared LLM Configuration for All Notebooks
==========================================================
Import this module in each notebook to get a properly configured litellm
environment. Automatically detects LiteLLM proxy credentials (Azure AD)
and routes all calls through the proxy when available.

Features:
  - Azure AD client-credentials token for LiteLLM proxy
  - Zscaler / corporate SSL certificate support
  - Global litellm configuration (api_base, api_key)
  - LangChain helpers (get_langchain_llm, get_langchain_embeddings)

Usage:
    from setup_llm import DEFAULT_MODEL, DEFAULT_EMBEDDING, is_proxy_mode
"""

import os
import sys
import ssl
import requests
from dotenv import load_dotenv
import litellm

# ─── Load Environment ─────────────────────────────────────────────────────────
load_dotenv()

# ─── Zscaler / Corporate SSL Certificate ─────────────────────────────────────
# Set REQUESTS_CA_BUNDLE or SSL_CERT_FILE in .env to point to your .pem file
# Example: REQUESTS_CA_BUNDLE=C:/certs/zscaler_root_ca.pem

_ssl_cert = os.getenv("REQUESTS_CA_BUNDLE") or os.getenv("SSL_CERT_FILE")
if _ssl_cert:
    if not os.path.isfile(_ssl_cert):
        print(f"⚠️ SSL cert file not found: {_ssl_cert}")
    else:
        # Set for requests library
        os.environ["REQUESTS_CA_BUNDLE"] = _ssl_cert
        # Set for httpx (used internally by litellm/openai SDK)
        os.environ["SSL_CERT_FILE"] = _ssl_cert
        # Set for pip/urllib3
        os.environ["CURL_CA_BUNDLE"] = _ssl_cert
        print(f"🔒 SSL: Using custom CA bundle: {os.path.basename(_ssl_cert)}")

# ─── Configuration ────────────────────────────────────────────────────────────
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
DEFAULT_EMBEDDING = os.getenv("DEFAULT_EMBEDDING_MODEL", "text-embedding-3-small")

# ─── Internal State ───────────────────────────────────────────────────────────
_proxy_active = False
_proxy_token = None
_proxy_url = None


def is_proxy_mode() -> bool:
    """Check if LiteLLM proxy mode is active."""
    return _proxy_active


def get_proxy_token() -> str:
    """Get the current proxy token (for use with LangChain, etc.)."""
    return _proxy_token


def _get_azure_token() -> str:
    """Fetch an Azure AD access token using client credentials."""
    tenant_id = os.getenv("AZURE_TENANT_ID")
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    try:
        response = requests.post(token_url, data={
            "grant_type": "client_credentials",
            "client_id": os.getenv("AZURE_CLIENT_ID"),
            "client_secret": os.getenv("AZURE_CLIENT_SECRET"),
            "scope": os.getenv("AZURE_SCOPE"),
        })

        if response.status_code != 200:
            print(f"⚠️ Azure AD token request failed ({response.status_code}): {response.text[:200]}")
            return None

        token = response.json().get("access_token")
        if token:
            print(f"🎫 Azure AD token acquired (length: {len(token)})")
        return token

    except requests.exceptions.SSLError as e:
        print(f"❌ SSL Error fetching Azure token: {e}")
        print(f"   💡 If behind Zscaler, set REQUESTS_CA_BUNDLE=path/to/zscaler.pem in .env")
        return None
    except Exception as e:
        print(f"⚠️ Azure AD token error: {e}")
        return None


def _configure_proxy():
    """
    Configure litellm to route ALL calls through the proxy.

    How it works:
      1. Sets litellm.api_base → proxy URL (overrides per-provider endpoints)
      2. Sets litellm.api_key  → Azure AD token (authenticates with proxy)

    After this, every litellm.completion() and litellm.embedding() call
    in any notebook automatically hits the proxy — no per-call changes needed.
    """
    global _proxy_active, _proxy_token, _proxy_url

    proxy_url = os.getenv("LITELLM_PROXY_URL", "").rstrip("/")
    has_azure_creds = all([
        os.getenv("AZURE_TENANT_ID"),
        os.getenv("AZURE_CLIENT_ID"),
        os.getenv("AZURE_CLIENT_SECRET"),
        os.getenv("AZURE_SCOPE"),
    ])

    if not proxy_url:
        return  # No proxy configured, use direct provider keys

    _proxy_url = proxy_url

    if has_azure_creds:
        # Fetch Azure AD token
        token = _get_azure_token()
        if token:
            _proxy_token = token

            # ╔══════════════════════════════════════════════════════════════╗
            # ║  THIS IS WHERE THE MAGIC HAPPENS                           ║
            # ║                                                            ║
            # ║  Setting these litellm globals means EVERY call to         ║
            # ║  litellm.completion() or litellm.embedding() anywhere      ║
            # ║  in any notebook will automatically use the proxy.         ║
            # ║                                                            ║
            # ║  The notebooks don't need to pass api_base or api_key —    ║
            # ║  litellm reads these module-level variables by default.    ║
            # ╚══════════════════════════════════════════════════════════════╝
            litellm.api_base = proxy_url
            litellm.api_key = token

            _proxy_active = True
            print(f"✅ litellm.api_base → {proxy_url}")
            print(f"✅ litellm.api_key  → Bearer <azure_token> (auto-injected into all calls)")
            return

    # Proxy URL set but no Azure creds — try using proxy with existing key
    litellm_key = os.getenv("LITELLM_API_KEY")
    if litellm_key:
        litellm.api_base = proxy_url
        litellm.api_key = litellm_key
        _proxy_active = True
        print(f"✅ litellm.api_base → {proxy_url}")
        print(f"✅ litellm.api_key  → LITELLM_API_KEY (auto-injected into all calls)")


def get_langchain_llm(model=None, temperature=0):
    """
    Get a LangChain ChatOpenAI instance configured for proxy or direct mode.

    In proxy mode, this points ChatOpenAI at your LiteLLM proxy
    with the Azure AD token as the API key.

    Usage:
        from setup_llm import get_langchain_llm
        llm = get_langchain_llm()
    """
    from langchain_openai import ChatOpenAI

    model = model or DEFAULT_MODEL
    kwargs = {"model": model, "temperature": temperature}

    if _proxy_active:
        kwargs["openai_api_base"] = _proxy_url
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
        kwargs["openai_api_base"] = _proxy_url
        kwargs["openai_api_key"] = _proxy_token or os.getenv("LITELLM_API_KEY", "sk-placeholder")

    return OpenAIEmbeddings(**kwargs)


# ─── Auto-configure on import ────────────────────────────────────────────────
_configure_proxy()

# ─── Print Status ─────────────────────────────────────────────────────────────
print()
if _proxy_active:
    print(f"🔗 LiteLLM Proxy Mode: {_proxy_url}")
    print(f"   Model: {DEFAULT_MODEL} | Embedding: {DEFAULT_EMBEDDING}")
    print(f"   All litellm.completion() calls auto-route through proxy ✅")
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
    print("\n" + "=" * 60)
    print("  setup_llm.py — Diagnostics")
    print("=" * 60)

    print(f"\n📋 Configuration:")
    print(f"   Proxy active:    {is_proxy_mode()}")
    print(f"   DEFAULT_MODEL:   {DEFAULT_MODEL}")
    print(f"   DEFAULT_EMBED:   {DEFAULT_EMBEDDING}")
    print(f"   SSL cert:        {_ssl_cert or 'system default'}")
    print(f"   litellm.api_base: {litellm.api_base}")
    print(f"   litellm.api_key:  {'<set>' if litellm.api_key else '<not set>'}")

    # Quick smoke test
    print(f"\n🧪 Smoke test (calling {DEFAULT_MODEL})...")
    try:
        response = litellm.completion(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": "Say 'hello' in one word."}],
            max_tokens=10,
        )
        print(f"   ✅ Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
