# Deep Agents + RAG Course

## Course Overview

A hands-on Jupyter notebook course covering LLMs, RAG, agent architectures, and production engineering. **24 notebooks · 8 phases · 4 capstone projects.**

## ⚡ Quick Start

```bash
cd agents-course
pip install -r requirements.txt
cp .env.example .env   # Add your API keys
jupyter notebook        # Start learning!
```

## 🔑 Multi-Model Setup

This course supports **OpenAI, Google Gemini, and Anthropic Claude** via `litellm`. Configure in `.env`:

```bash
# Pick your provider (at least one required)
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AI...
ANTHROPIC_API_KEY=sk-ant-...

# Default model (used by all notebooks)
DEFAULT_MODEL=gpt-4o-mini       # or gemini/gemini-2.0-flash or anthropic/claude-3-5-sonnet-20241022
```

### 🔗 LiteLLM Proxy Mode (Optional)

If your org provides a **LiteLLM proxy** secured behind Azure AD, all notebooks can route through it automatically. Add these to `.env`:

```bash
AZURE_TENANT_ID=your-azure-tenant-id
AZURE_CLIENT_ID=your-azure-client-id
AZURE_CLIENT_SECRET=your-azure-client-secret
AZURE_SCOPE=api://your-litellm-app-id/.default
LITELLM_PROXY_URL=https://your-litellm-proxy.example.com
```

When these are set, the shared [`setup_llm.py`](./setup_llm.py) module:
1. Fetches an Azure AD token using the client credentials flow
2. Configures `litellm` globally to route through your proxy
3. All notebooks automatically use the proxy — no per-notebook changes needed

When they are **not** set, everything falls back to direct API keys (no behavior change).

| Mode | When Active | How It Works |
|------|-------------|-------------|
| 🔑 **Direct** | `LITELLM_PROXY_URL` not set | Calls OpenAI/Gemini/Claude directly using API keys |
| 🔗 **Proxy** | `LITELLM_PROXY_URL` + Azure creds set | Routes all calls through LiteLLM proxy |

### Proxy Setup Reference

| File | Purpose |
|------|---------|
| [`setup_llm.py`](./setup_llm.py) | Shared config module — imported by all notebooks |
| [`azure_litellm_auth.py`](./azure_litellm_auth.py) | Standalone helper to test Azure AD → LiteLLM auth |
| [`.env.example`](./.env.example) | Template with all supported environment variables |

## 📚 Course Structure

### Phase 1 — LLM Fundamentals
| # | Notebook | Topics |
|---|----------|--------|
| 01 | `01_llm_basics.ipynb` | API calls, tokenization, temperature, prompt engineering |
| 02 | `02_structured_output.ipynb` | JSON mode, function calling, Pydantic, guardrails |
| 03 | `03_embeddings.ipynb` | Vector spaces, similarity metrics, semantic search |

### Phase 2 — RAG
| # | Notebook | Topics |
|---|----------|--------|
| 04 | `04_basic_rag.ipynb` | Chunking, retrieval, context injection |
| 05 | `05_advanced_rag.ipynb` | Hybrid search, reranking, query transformation |
| 06 | `06_vector_db.ipynb` | FAISS, ChromaDB, ANN algorithms, persistence |

### Phase 3 — Tools & Function Calling
| # | Notebook | Topics |
|---|----------|--------|
| 07 | `07_tools.ipynb` | Tool schemas, execution loop, error handling |
| 08 | `08_react_agent.ipynb` | ReAct pattern, multi-step reasoning |

### Phase 4 — Agent Architecture
| # | Notebook | Topics |
|---|----------|--------|
| 09 | `09_memory.ipynb` | Buffer, window, summary, vector memory |
| 10 | `10_planning_agent.ipynb` | Task decomposition, Planner-Executor |
| 11 | `11_multi_agent.ipynb` | Manager-Worker, fan-out/fan-in |

### Phase 5 — Advanced Deep Agent Concepts
| # | Notebook | Topics |
|---|----------|--------|
| 12 | `12_reflection.ipynb` | Self-critique, reflection loops |
| 13 | `13_toolformer.ipynb` | Dynamic tool discovery, Toolformer |
| 14 | `14_filesystem_agent.ipynb` | Sandboxed file I/O, code generation |

### Phase 6 — Production Engineering
| # | Notebook | Topics |
|---|----------|--------|
| 15 | `15_evaluation.ipynb` | RAG metrics, LLM-as-Judge, hallucination detection |
| 16 | `16_guardrails.ipynb` | Prompt injection, defense-in-depth |
| 17 | `17_optimization.ipynb` | Semantic caching, streaming, batch embedding |

### Phase 7 — Industry Frameworks
| # | Notebook | Topics |
|---|----------|--------|
| 18 | `18_langchain_core.ipynb` | LCEL, chat models, agents, memory |
| 19 | `19_langchain_rag.ipynb` | Loaders, splitters, retrieval chains |
| 20 | `20_langgraph.ipynb` | State graphs, checkpointing, human-in-the-loop |
| 21 | `21_langsmith.ipynb` | Tracing, evaluation, monitoring |
| 22 | `22_industry_frameworks.ipynb` | LlamaIndex, CrewAI, AutoGen, DSPy *(informational — no LLM calls)* |

### Phase 8 — Deep Agent Patterns
| # | Notebook | Topics |
|---|----------|--------|
| 23 | `23_deep_agents.ipynb` | Agentic RAG, autonomous loops, MCP, A2A, swarm |
| 24 | `24_deepagents.ipynb` | DeepAgents library — planning, filesystem, subagents |

### 🏆 Capstone Projects
| # | Project | Applies |
|---|---------|---------| 
| C1 | Document Q&A System | NB 01-06 |
| C2 | Multi-Agent Research System | NB 07-14 |
| C3 | Production RAG Agent | All fundamentals |
| C4 | LangGraph Production Agent | NB 18-23 |

### ⏭️ Notebooks Without Proxy Integration

| Notebook | Reason |
|----------|--------|
| `22_industry_frameworks.ipynb` | Purely informational — no LLM API calls, just static framework comparisons |

All other 27 notebooks (01-21, 23-24, Capstone 1-4) use `setup_llm.py` and fully support proxy mode.

## 📋 Reference
- **[TOPICS_GUIDE.md](./TOPICS_GUIDE.md)** — Complete list of every concept covered
- **[SKILL.md](./SKILL.md)** — Study guide and learning path
- **[CLAUDE.md](./CLAUDE.md)** — AI assistant instructions for this project
