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
| 22 | `22_industry_frameworks.ipynb` | LlamaIndex, CrewAI, AutoGen, DSPy |

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

## 📋 Reference
- **[TOPICS_GUIDE.md](./TOPICS_GUIDE.md)** — Complete list of every concept covered
- **[SKILL.md](./SKILL.md)** — Study guide and learning path
- **[CLAUDE.md](./CLAUDE.md)** — AI assistant instructions for this project
