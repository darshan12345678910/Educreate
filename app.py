import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ingest import ingest_pdf
from generate_questions import load_bot
from chat_with_pdf import load_chat_bot, chat_with_pdf
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('pdf_file')
        question_type = request.form.get('question_type')

        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Step 1: Create FAISS vector store
            ingest_pdf(filepath)

            try:
                # Step 2: Load chain only after ingestion
                qa_chain = load_bot(prompt_type=question_type)
                response = qa_chain.run("Generate questions from this content")
                return render_template('result.html', questions=response)
            except FileNotFoundError:
                return render_template('index.html', error="Error: Vector store not found.")
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    error = None
    answer = None
    question = None

    # Check if vector store exists before chatting
    if not Path("vector_store/index.faiss").exists():
        error = "Upload a PDF first to enable chat."
        return render_template('chat.html', error=error)

    chat_chain = load_chat_bot()

    if request.method == 'POST':
        question = request.form.get('user_question')
        if question:
            answer = chat_with_pdf(question, chat_chain)
        else:
            error = "Please enter a question."

    return render_template('chat.html', question=question, answer=answer, error=error)


if __name__ == "__main__":
    app.run()

