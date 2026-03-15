from pdf_processor import extract_text, split_text
from vectorstore import build_vectordb, search, get_vectordb
from llm import get_answer

PDF_PATH = "college dataset.pdf"


def initialize():
    text = extract_text(PDF_PATH)
    if not text.strip():
        print("⚠️ Could not extract text from college dataset.pdf")
        return
    chunks = split_text(text)
    build_vectordb(chunks)
    print(f"✅ college dataset.pdf loaded! {len(chunks)} chunks indexed.")


def ask(query: str) -> str:
    if get_vectordb() is None:
        return "⚠️ PDF not loaded. Make sure college dataset.pdf is in the Space."
    if not query.strip():
        return "⚠️ Please enter a question."

    docs = search(query)
    context = "\n".join([doc.page_content for doc in docs])
    return get_answer(context, query)


initialize()