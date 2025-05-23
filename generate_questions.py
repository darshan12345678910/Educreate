import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import re

load_dotenv(override=True)
groq_api_key = os.getenv("GROQ_API_KEY")

BLOOMS_TEMPLATE = """You are a teaching assistant.

Generate one question from each level of Bloom’s Taxonomy based on the following content:

1. Remember
2. Understand
3. Apply
4. Analyze
5. Evaluate
6. Create

Context:
{context}

Output only the 6 questions, clearly labeled by Bloom's level.
"""
MCQ_PROMPT = """
You are an educational AI.

Generate 5 multiple-choice questions (MCQs) based on the following content. Each question must have:
- 1 correct answer
- 3 plausible distractors (wrong answers)
- A clear format:

Question:
A) Option 1  
B) Option 2  
C) Option 3  
D) Option 4  
Answer: [Correct Option Letter]

Content:
{context}
"""
def load_bot(prompt_type="bloom", vectorstore_path="vector_store"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(vectorstore_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()

    if prompt_type == "mcq":
        prompt = PromptTemplate(input_variables=["context"], template=MCQ_PROMPT)
    else:
        prompt = PromptTemplate(input_variables=["context"], template=BLOOMS_TEMPLATE)

    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain
