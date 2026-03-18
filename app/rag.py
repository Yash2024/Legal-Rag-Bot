from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "faiss_index")

db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 7}
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, question):
    prompt = f"""
You are a legal expert specializing in Bharatiya Nyaya Sanhita (BNS).

STRICT RULES:
- Answer ONLY from the provided context
- Do NOT make up anything
- If answer is not clearly present, say: "Not available in BNS"
- Quote relevant section text if possible
- Keep answer precise and structured

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def rag_pipeline(question):
    docs = retriever.invoke(question)
    docs = docs[:5]
    context = ""
    sources = []

    for doc in docs:
        context += doc.page_content + "\n\n"
        sources.append(f"{doc.metadata.get('source')} (page {doc.metadata.get('page')})")

    answer = generate_answer(context, question)

    return {
        "answer": answer,
        "sources": list(set(sources))
    }