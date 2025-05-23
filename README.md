# Educreate
## PDF Chatbot with LangChain & HuggingFace

This project enables you to chat with the content of a PDF document using state-of-the-art language models and vector search. It uses LangChain for chaining, HuggingFace embeddings, FAISS for vector search, and a Groq-powered LLM for answering user queries based on PDF content.

---

## Features

- Load PDF content as a vector store (FAISS) with HuggingFace sentence embeddings
- Conversational Q&A over PDF content with custom prompt templates
- Structured output parsing for different question types (MCQ, short answer, long answer, true/false, fill-in-the-blanks)
- Easily extendable for UI integration or API use

---

## Requirements

- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
