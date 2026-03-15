from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import EMBEDDING_MODEL

embedding = None
vectordb = None


def get_embedding():
    global embedding
    if embedding is None:
        embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return embedding


def build_vectordb(chunks: list):
    global vectordb
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=get_embedding()
    )
    return vectordb


def get_vectordb():
    return vectordb


def search(query: str, k: int = 8) -> list:
    if vectordb is None:
        return []
    return vectordb.similarity_search(query, k=k)