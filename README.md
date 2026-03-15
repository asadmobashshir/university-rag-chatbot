🎓 University RAG Chatbot

An AI-powered chatbot that answers university-related queries such as admissions, courses, fees, and placements using Retrieval-Augmented Generation (RAG).

The chatbot retrieves relevant information from a college dataset PDF and generates accurate responses using the Mistral 7B language model.

🚀 Features

Answer questions about admissions, departments, courses, and placements

Uses Retrieval-Augmented Generation (RAG) for accurate responses

Retrieves information from a PDF dataset

Fast semantic search using vector embeddings

Interactive chatbot interface

🧠 Technologies Used

LLM: Mistral 7B

Embeddings: MiniLM-L6

Vector Database: ChromaDB

Framework: Hugging Face Spaces

Language: Python

Interface: Gradio

⚙️ How It Works

The college dataset PDF is loaded and split into smaller chunks.

Each chunk is converted into vector embeddings using MiniLM.

Embeddings are stored in ChromaDB vector database.

When a user asks a question:

The system retrieves the most relevant chunks.

These chunks are sent to Mistral 7B.

The model generates a context-aware answer.

📂 Project Structure
university-rag-chatbot
│
├── app.py
├── requirements.txt
├── college_dataset.pdf
├── chroma_db
└── README.md
▶️ Installation

Clone the repository:

git clone https://github.com/asadmobashshir/university-rag-chatbot.git

Go into the project folder:

cd university-rag-chatbot

Install dependencies:

pip install -r requirements.txt

Run the chatbot:

python app.py
💬 Example Questions

What is the admission process?

What courses are available?

What is the placement package?

Does the university provide hostel facilities?

🌐 Deployment

This chatbot is deployed using Hugging Face Spaces.

📌 Future Improvements

Add multiple university datasets

Improve UI design

Add voice interaction

Integrate more advanced LLMs

👨‍💻 Author

Mobashshir Asad
AI / Machine Learning Enthusiast

GitHub:
https://github.com/asadmobashshir
