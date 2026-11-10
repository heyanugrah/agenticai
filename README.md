# Agentic AI Experiments

This repository is a collection of small LangGraph-based AI experiments and proof-of-concepts exploring agent workflows, retrieval-augmented generation, workflow orchestration, and iterative review loops.

The project is intended for learning and experimentation with modern LLM tooling in Python.

## Overview

These scripts demonstrate different patterns:

- Sequential multi-step processing pipelines
- Conditional routing and graph-based workflows
- Retrieval-augmented generation (RAG)
- Parallel analysis branches
- Iterative drafting and review loops
- State management patterns for LangGraph agents

## Project Structure

- `sequential_base.py`  
  A simple three-stage workflow: edit text -> write script -> localize to Hinglish.

- `iterative.py`  
  A LinkedIn post generator that drafts content, reviews it, and revises it until approved.

- `conditional_RAG.py`  
  A college assistant using RAG over PDF documents for academic and fee-related queries.

- `parallel_reducers.py`  
  A parallel safety-scoring workflow that evaluates text across multiple dimensions.

- `main.py`  
  Placeholder/sample script; not a full application.

- `states.py`  
  Notes and examples about different state patterns in LangGraph.

- `academics_handbook.pdf`  
  Academic policy/reference document used by the RAG example.

- `fee_structure.pdf`  
  Fee-related document used by the RAG example.

- `.env`  
  Local environment variables for API keys and service configuration.

## Tech Stack

- Python
- LangChain
- LangGraph
- Groq LLM API
- Google Gemini
- Hugging Face embeddings
- FAISS vector store
- PyPDF for document loading
- Tavily for web search

## Requirements

Python 3.10+ is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root and add your API keys. Example:

```env
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_key
```

Some scripts may require additional configuration depending on the model or service used.

## Running the Examples

### 1. Sequential workflow

```bash
python sequential_base.py
```

### 2. Iterative drafting workflow

```bash
python iterative.py
```

### 3. Conditional RAG

```bash
python conditional_RAG.py
```

### 4. Parallel safety analysis

```bash
python parallel_reducers.py
```

## Notes

- This is primarily a learning repository for agentic AI patterns.
- Not all scripts are production-ready applications.
- Some examples are intentionally experimental and may need small fixes depending on package versions or API changes.
- The project uses external LLM providers; ensure your keys are valid and have the required quota.

## Typical Use Cases Covered

- Prompt-driven content generation
- Graph orchestration for business workflows
- Document-grounded Q&A using RAG
- Multi-stage AI reasoning and review
- Parallel branching for analysis tasks

## Future Improvements

- Add a proper CLI interface
- Standardize script entry points
- Add tests and validation for each workflow
- Improve error handling and API fallback logic
- Package reusable agents and utility functions

## License

This project is for educational and experimental purposes.
