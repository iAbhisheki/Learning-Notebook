# SKILL.md — Deep Agents + RAG Course Study Guide

## 🎯 What This Course Covers

A complete learning path from **LLM basics to production-grade agent systems**, covering every concept asked in AI/ML engineering interviews.

---

## 📖 Recommended Learning Path

### Beginner Track (Start Here)
If you're new to LLMs and AI agents:
```
NB01 → NB02 → NB03 → NB04 → NB06 → NB07 → NB08
```
**Time:** ~2 weeks (1 notebook/day)

### Intermediate Track
If you know LLM basics but want to build agents:
```
NB04 → NB05 → NB06 → NB07 → NB08 → NB09 → NB10 → NB11
```
**Time:** ~1.5 weeks

### Advanced Track
If you know agents and want production + frameworks:
```
NB12 → NB15 → NB16 → NB17 → NB18 → NB19 → NB20 → NB21 → NB23 → NB24
```
**Time:** ~1.5 weeks

### Interview Prep Track (Most Common Questions)
Focus on the most frequently asked topics:
```
NB01 (LLM basics) → NB04 (RAG) → NB03 (Embeddings) → NB06 (Vector DBs)
→ NB08 (ReAct) → NB09 (Memory) → NB18 (LangChain) → NB20 (LangGraph)
→ NB23 (Deep Agents) → NB24 (DeepAgents Library) → NB22 (Framework Comparison)
```

### Full Course
Go sequentially: `NB01 → NB02 → ... → NB23 → Capstones`
**Time:** ~4-5 weeks

---

## 🧠 Key Concepts by Interview Frequency

### 🔴 Asked in Nearly Every Interview
- RAG architecture (NB04)
- Chunking strategies (NB04)
- Vector similarity / embeddings (NB03)
- LangChain LCEL (NB18)
- LangGraph basics (NB20)
- Prompt engineering (NB01)
- Hallucination and mitigation (NB15)

### 🟡 Asked Frequently
- Hybrid search (NB05)
- ReAct agent pattern (NB08)
- Memory types (NB09)
- Prompt injection defense (NB16)
- LLM evaluation metrics (NB15)
- LangSmith tracing (NB21)
- Agentic RAG (NB23)

### 🟢 Differentiators (Impress the Interviewer)
- Multi-agent patterns — supervisor vs swarm (NB11, NB23)
- MCP and A2A protocols (NB23)
- Semantic caching (NB17)
- Framework comparison (NB22)
- DSPy and programmatic prompt optimization (NB22)
- Agent evaluation benchmarks (NB23)

---

## 🏗️ Build Projects Summary

Every notebook has a hands-on build. Here's what you'll create:

| NB | Build Project |
|----|--------------|
| 01 | Multi-model Q&A chatbot |
| 02 | ETL JSON extractor |
| 03 | Semantic search engine |
| 04 | RAG over documents |
| 05 | Advanced RAG pipeline |
| 06 | Persistent knowledge base |
| 07 | Multi-tool agent |
| 08 | Research assistant |
| 09 | Persistent personal assistant |
| 10 | Planner-Executor agent |
| 11 | Research team simulator |
| 12 | Self-improving answer agent |
| 13 | Dynamic tool discovery agent |
| 14 | Mini AutoGPT coding agent |
| 15 | RAG evaluation harness |
| 16 | Hardened bot with guardrails |
| 17 | Optimized RAG pipeline |
| 18 | LangChain multi-model chatbot |
| 19 | LangChain RAG pipeline |
| 20 | LangGraph ReAct agent |
| 21 | Observability pipeline |
| 22 | Framework comparison demo |
| 23 | Autonomous research agent |
| 24 | Deep agent for complex research tasks |

---

## 📝 How to Study Each Notebook

1. **Read the theory sections** — understand the concepts
2. **Run every code cell** — hands-on learning
3. **Complete the interview quiz** — test your understanding (don't peek at answers first!)
4. **Modify the build project** — extend it with your own ideas
5. **Review the summary table** — quick reference for revision

---

## 🛠️ Prerequisites

- Python 3.10+
- Basic Python (classes, functions, decorators)
- API key from at least one: OpenAI, Google AI, or Anthropic
- `pip install -r requirements.txt`

---

## 📂 File Structure

```
agents-course/
├── 01_llm_basics.ipynb          # Phase 1: LLM Fundamentals
├── 02_structured_output.ipynb
├── 03_embeddings.ipynb
├── 04_basic_rag.ipynb           # Phase 2: RAG
├── 05_advanced_rag.ipynb
├── 06_vector_db.ipynb
├── 07_tools.ipynb               # Phase 3: Tools
├── 08_react_agent.ipynb
├── 09_memory.ipynb              # Phase 4: Architecture
├── 10_planning_agent.ipynb
├── 11_multi_agent.ipynb
├── 12_reflection.ipynb          # Phase 5: Advanced
├── 13_toolformer.ipynb
├── 14_filesystem_agent.ipynb
├── 15_evaluation.ipynb          # Phase 6: Production
├── 16_guardrails.ipynb
├── 17_optimization.ipynb
├── 18_langchain_core.ipynb      # Phase 7: Frameworks
├── 19_langchain_rag.ipynb
├── 20_langgraph.ipynb
├── 21_langsmith.ipynb
├── 22_industry_frameworks.ipynb
├── 23_deep_agents.ipynb         # Phase 8: Deep Agents
├── 24_deepagents.ipynb          # Phase 8: DeepAgents Library
├── capstone/
│   ├── capstone_1_document_qa.ipynb
│   ├── capstone_2_research_agents.ipynb
│   ├── capstone_3_production_agent.ipynb
│   └── capstone_4_langgraph_agent.ipynb
├── requirements.txt
├── .env.example
├── README.md
├── SKILL.md                     # This file
├── CLAUDE.md                    # AI assistant context
└── TOPICS_GUIDE.md              # Full concept reference
```
