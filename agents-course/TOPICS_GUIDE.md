# 📚 Deep Agents + RAG Course — Complete Topics Guide

> **24 Notebooks · 8 Phases · 4 Capstone Projects**
> Every topic below is covered with runnable code, interview quizzes, and hands-on builds.

---

## Phase 1 — LLM Fundamentals

### NB01 · LLM Basics
- LLM API calls (OpenAI, Google Gemini, Anthropic Claude)
- Multi-model setup with `litellm` wrapper
- Tokenization (`tiktoken`, token counting, token economics)
- Temperature, top_p, top_k sampling parameters
- System prompts vs user prompts
- Prompt engineering techniques:
  - Zero-shot prompting
  - Few-shot prompting
  - Chain-of-Thought (CoT) prompting
  - Self-consistency prompting
- Role-based prompt design
- 🏗️ **Build:** Multi-model Q&A chatbot

### NB02 · Structured Output
- JSON mode (`response_format`)
- Function calling / tool use
- `tool_choice` options (auto, required, specific)
- Pydantic schema validation
- Runtime type checking & guardrails
- Error handling for malformed LLM output
- OutputFixingParser pattern
- 🏗️ **Build:** ETL-style JSON extractor

### NB03 · Embeddings & Semantic Search
- What are vector embeddings (geometric intuition)
- Embedding models (OpenAI, Sentence-Transformers)
- Distance metrics:
  - Cosine similarity
  - Dot product
  - Euclidean distance
- Batch embedding for efficiency
- PCA visualization of embedding spaces
- Curse of dimensionality
- Multilingual embeddings
- 🏗️ **Build:** In-memory semantic search engine

---

## Phase 2 — RAG (Retrieval Augmented Generation)

### NB04 · Basic RAG
- RAG architecture overview
- Why RAG over fine-tuning
- Chunking strategies:
  - Fixed-size chunking
  - Recursive character splitting
  - Sentence-based chunking
  - Semantic chunking
- Chunk size and overlap tuning
- Embedding chunks into vector space
- Similarity search retrieval
- Context injection into LLM prompt
- Citation and source tracking
- 🏗️ **Build:** RAG over PDF/TXT documents

### NB05 · Advanced RAG
- Hybrid search (BM25 keyword + semantic)
- Metadata filtering
- Re-ranking retrieved results
- Query transformation techniques:
  - Query decomposition
  - HyDE (Hypothetical Document Embeddings)
  - Step-back prompting
- Context window optimization
- Multi-query retrieval
- 🏗️ **Build:** Advanced RAG pipeline with hybrid search

### NB06 · Vector Databases
- FAISS (Facebook AI Similarity Search)
  - IndexFlatL2, IndexIVFFlat, IndexHNSW
- ChromaDB
  - Collections, metadata, persistence
- ANN algorithms:
  - Flat (brute force)
  - IVF (Inverted File Index)
  - HNSW (Hierarchical Navigable Small World)
- Persistence and serialization
- Cloud vector DBs (Pinecone, Weaviate, Qdrant)
- 🏗️ **Build:** Persistent knowledge base

---

## Phase 3 — Tools & Function Calling

### NB07 · Tool Usage
- Tool definition via JSON Schema
- The tool execution loop: Call → Execute → Return → Answer
- Error handling and retry strategies
- Multiple tool management
- `tool_choice` parameter (auto, none, required, specific)
- Tool safety: allowlists, rate limits, sandboxing
- Tool registry pattern
- 🏗️ **Build:** Agent with search, math, and API tools

### NB08 · ReAct Agent
- ReAct pattern: Thought → Action → Observation
- Multi-step reasoning chains
- Comparison: ReAct vs CoT vs Plan-then-Execute vs Reflexion
- Agent trace logging and observability
- Metrics: latency, rounds, tool calls
- Parallel tool calls
- Loop prevention (max rounds, cycle detection)
- 🏗️ **Build:** Research assistant agent

---

## Phase 4 — Agent Architecture

### NB09 · Memory
- Short-term memory:
  - Buffer memory (full history)
  - Window memory (last N messages)
- Long-term memory:
  - Summary memory (compressed context)
  - Vector memory (semantic similarity retrieval)
- Hybrid memory architecture
- Fact extraction for long-term storage
- Persistent memory (save/load)
- Token budget management
- 🏗️ **Build:** Persistent personal assistant

### NB10 · Planning Agents
- Task decomposition with LLM
- Dependency graphs (DAG)
- Planner-Executor architecture
- Topological ordering for step execution
- Re-planning on failure
- Adaptive plan modification
- Plan step parallelization
- 🏗️ **Build:** Planner-Executor agent

### NB11 · Multi-Agent Systems
- Manager-Worker pattern (hierarchical)
- Peer-to-peer pattern (decentralized)
- Fan-out / Fan-in pattern (parallel aggregate)
- Pipeline pattern (sequential handoff)
- Agent specialization and role design
- Dynamic task-to-agent routing
- Agent communication protocols
- Cost-quality trade-offs of multi-agent systems
- 🏗️ **Build:** Research team simulator

---

## Phase 5 — Advanced Deep Agent Concepts

### NB12 · Reflection & Self-Improvement
- Self-critique pattern
- Generate → Critique → Improve loop
- Structured critique (JSON with score, strengths, weaknesses)
- Convergence detection (quality threshold, diminishing returns)
- Over-editing risk and mitigation
- Inference-time compute scaling vs RLHF
- 🏗️ **Build:** Self-improving answer agent

### NB13 · Toolformer Style Agents
- Dynamic tool registry (register/unregister at runtime)
- Tool discovery by tag and capability
- Conditional tool usage (only when beneficial)
- Tool selection via LLM relevance assessment
- Tool composition and chaining
- Scaling tool sets without context overflow
- 🏗️ **Build:** Dynamic tool discovery agent

### NB14 · Filesystem Agents
- Sandboxed filesystem operations
- Path traversal prevention
- Code generation by LLM
- Subprocess-based code execution
- Auto-debugging: error feedback loop
- Safety: timeout, output limits, no network
- Production sandboxing (Docker, WASM, Firecracker)
- 🏗️ **Build:** Mini AutoGPT coding agent

---

## Phase 6 — Production Engineering

### NB15 · Evaluation
- RAG evaluation framework:
  - Faithfulness (supported by context?)
  - Answer relevance (addresses question?)
  - Retrieval precision and recall
- Hallucination detection
- LLM-as-Judge pattern (pros, cons, biases)
- Building golden test datasets
- Batch evaluation pipelines
- Production RAG dashboards
- 🏗️ **Build:** RAG evaluation harness

### NB16 · Guardrails & Security
- Prompt injection attacks (direct & indirect)
- Jailbreak techniques and defenses
- Input guardrails:
  - Regex pattern matching
  - Length limits and banned words
  - Intent classification
- Output guardrails:
  - Safety checking
  - PII detection
  - Topic relevance validation
- Defense-in-depth architecture (6 layers)
- Sandwiched prompt pattern
- Indirect injection via RAG
- 🏗️ **Build:** Hardened bot with guardrails

### NB17 · Performance Optimization
- Semantic caching (embedding-based deduplication)
- Exact vs semantic cache comparison
- Token reduction strategies:
  - Prompt compression
  - Context pruning by relevance
  - System prompt optimization
- Streaming responses (stream=True)
- Batch embedding (10-50x speedup)
- Multi-model cost routing
- 🏗️ **Build:** Optimized RAG pipeline with caching

---

## Phase 7 — Industry Frameworks

### NB18 · LangChain Core
- Chat models (unified interface across providers)
- `invoke()`, `batch()`, `stream()` API
- Prompt templates and `MessagesPlaceholder`
- LCEL (LangChain Expression Language):
  - Pipe operator `|` composition
  - `RunnablePassthrough`, `RunnableLambda`, `RunnableParallel`
- Output parsers:
  - `StrOutputParser`, `JsonOutputParser`
  - `PydanticOutputParser` with schema enforcement
- LangChain Tools (`@tool` decorator)
- `AgentExecutor` for tool-calling agents
- Conversation memory (`RunnableWithMessageHistory`)
- 🏗️ **Build:** Multi-model chatbot with LangChain

### NB19 · LangChain RAG
- Document loaders (TextLoader, PyPDFLoader, WebBaseLoader)
- Text splitters:
  - `RecursiveCharacterTextSplitter` (default)
  - `CharacterTextSplitter`, `TokenTextSplitter`
  - `MarkdownHeaderTextSplitter`, `SemanticChunker`
- LangChain embedding wrappers
- Vector stores via LangChain (Chroma, FAISS)
- Retriever abstraction (`.as_retriever()`)
- LCEL RAG chain composition
- Conversational RAG with history-aware retrieval
- Question reformulation for follow-ups
- 🏗️ **Build:** Production RAG pipeline with LangChain

### NB20 · LangGraph
- State graphs (StateGraph, TypedDict state)
- Nodes (Python functions) and edges
- Conditional edges (LLM-driven routing)
- Cycles and loops (ReAct, reflection)
- `create_react_agent` prebuilt pattern
- Custom multi-step agent graphs
- Checkpointing:
  - MemorySaver (dev), SqliteSaver, PostgresSaver
  - State persistence and resume
  - Time travel debugging
- Human-in-the-loop (`interrupt_before`)
- Multi-agent graphs (supervisor pattern)
- 🏗️ **Build:** ReAct agent with LangGraph

### NB21 · LangSmith + Observability
- Automatic tracing (LANGCHAIN_TRACING_V2)
- Trace structure: spans, parent-child relationships
- Run metadata and tagging
- Evaluation framework:
  - Test datasets creation
  - Custom evaluators (LLM-as-judge, heuristic)
  - Experiment tracking
- Production monitoring
- Alternatives: Langfuse, Phoenix, OpenTelemetry, W&B, Helicone
- Manual instrumentation pattern
- 🏗️ **Build:** Full observability pipeline

### NB22 · Industry Frameworks Overview
- **LlamaIndex:** Data connectors, index types, query engines
- **CrewAI:** Role-based agents (role, goal, backstory), delegation
- **AutoGen:** Conversable agents, group chat, code execution
- **DSPy:** Declarative prompt optimization, compile from examples
- **Haystack:** Pipeline-based NLP, enterprise search
- **Semantic Kernel:** Microsoft's AI SDK
- Framework comparison matrix (11 dimensions)
- Framework decision tree
- Production stack recommendations

---

## Phase 8 — Deep Agent Patterns

### NB23 · Deep Agents
- Agentic RAG:
  - Agent-controlled retrieval (IF, WHERE, HOW)
  - Query classification and routing
  - Multi-source retrieval
  - Multi-hop reasoning chains
- Autonomous agent loops:
  - Goal-directed cycles (Plan → Execute → Evaluate)
  - Progress tracking and re-planning
  - Convergence and stopping conditions
  - Runaway prevention (max iterations, cost limits)
- Supervisor pattern (centralized coordinator)
- Swarm pattern (decentralized handoffs, OpenAI Swarm-style)
- MCP (Model Context Protocol):
  - Resources, Tools, Prompts, Sampling
  - Server/client architecture
  - Use cases: database, filesystem, API integration
- A2A (Agent-to-Agent Protocol):
  - Agent Cards (capability discovery)
  - Task lifecycle (submit → working → done)
  - Message passing and artifact exchange
- Agent evaluation:
  - Task completion rate
  - Tool accuracy
  - Reasoning quality (LLM-as-judge on trace)
  - Efficiency (steps, tokens, latency)
  - Safety and reliability metrics
  - Benchmarks: SWE-Bench, GAIA, WebArena
- Agent-as-a-Service patterns
- 🏗️ **Build:** Autonomous research agent with goal tracking

### NB24 · DeepAgents Library
- `create_deep_agent` API — the core function
- TodoListMiddleware:
  - `write_todos` for dynamic task planning
  - Progress tracking and plan adaptation
- FilesystemMiddleware:
  - Virtual filesystem backend (in-memory, disk)
  - `write_file`, `read_file`, `edit_file`, `ls`, `glob`, `grep`
  - Context offloading to prevent overflow
- SubAgentMiddleware:
  - Spawning specialist subagents
  - Context isolation per subagent
  - Subtask delegation and result synthesis
- SummarizationMiddleware — conversation compression
- Custom tools alongside built-in tools
- LangGraph integration (checkpointing, streaming)
- Deep vs shallow agent comparison
- DeepAgents vs CrewAI vs AutoGen
- 🏗️ **Build:** Deep agent for complex research tasks

---

## Capstone Projects

### Capstone 1 — Intelligent Document Q&A System
> Applies: NB 01–06
- Multi-format document ingestion (PDF, TXT, MD)
- Chunking + embedding into ChromaDB
- Hybrid search retrieval
- RAG with source citations
- Self-evaluation (faithfulness + relevance)

### Capstone 2 — Multi-Agent Research System
> Applies: NB 07–14
- Manager agent (task decomposition)
- Researcher agents (parallel information gathering)
- Writer agent (report synthesis)
- Reviewer agent (quality scoring)
- Reflector agent (iterative improvement)
- Full trace logging

### Capstone 3 — Production RAG Agent
> Applies: ALL notebooks
- Full data pipeline (ingest → chunk → embed → store)
- Hybrid retrieval + reranking
- ReAct agent with tools and memory
- Input/output guardrails
- Evaluation scoring per response
- Semantic caching + streaming
- Observability and metrics

### Capstone 4 — LangGraph Production Agent
> Applies: NB 18–23
- LangGraph StateGraph with conditional routing
- LangChain RAG pipeline with Chroma
- Multi-agent supervisor pattern
- Reflection loop (improve if quality < 8)
- Input/output guardrail nodes
- LangGraph checkpointing for multi-turn
- LangSmith tracing and evaluation

---

## Cross-Cutting Concepts (Covered Throughout)

| Concept | Where Covered |
|---------|-------------|
| Multi-model support (OpenAI/Gemini/Claude) | Every notebook |
| Interview quiz blocks | Every notebook |
| Hands-on build exercises | Every notebook |
| Token economics & cost optimization | NB01, NB17, NB22 |
| Prompt engineering | NB01, NB02, NB13, NB18 |
| Error handling & retries | NB07, NB08, NB14 |
| Safety & security | NB14, NB16 |
| Production patterns | NB15–NB23 |
| Agent architectures comparison | NB08, NB10, NB11, NB22, NB23 |
| Framework selection guidance | NB22 |
| MCP & A2A protocols | NB23 |
| Autonomous agent patterns | NB12, NB14, NB23 |
