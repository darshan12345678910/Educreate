import os
from dotenv import load_dotenv
from ingest import ingest_pdf
from generate_questions import load_bot

load_dotenv(opoverride=True)
import os
groq_api_key = os.getenv("GROQ_API_KEY")


# Step 1: Ingest the PDF
ingest_pdf("data\\rnn_tutorial.pdf")

# Step 2: Load the chatbot with Groq + vector retrieval
qa_chain = load_bot()

# Step 3: Ask for Bloom’s taxonomy questions
query = "Generate Bloom’s taxonomy questions from this content"
response = qa_chain.run(query)

print("\n📘 Bloom’s Taxonomy Questions:\n")
print(response)
