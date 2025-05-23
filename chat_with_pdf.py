from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

def load_chat_bot(vectorstore_path="vector_store"):
    # Load embeddings and FAISS vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(
        vectorstore_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever()

    # Define prompt for conversational Q&A (can customize this)
    PROMPT = """You are an assistant helping with the content of a PDF document.
Answer the user question based only on the context provided.

Context:
{context}

User Question:
{question}

Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=PROMPT
    )

    # Initialize LLM model
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.3
    )

    # Create RetrievalQA chain with custom prompt
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain

def chat_with_pdf(query: str, chat_chain):
    # Run query through the chain and get answer
    response = chat_chain.run(query)
    return response


