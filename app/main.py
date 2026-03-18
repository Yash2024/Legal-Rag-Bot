from fastapi import FastAPI
from app.rag import rag_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Legal RAG API Running"}

@app.get("/ask")
def ask(question: str):
    result = rag_pipeline(question)
    return result