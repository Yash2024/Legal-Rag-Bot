from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


def load_all_pdfs(data_path):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_path, file))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = file

            documents.extend(docs)

    return documents


def ingest():
    documents = load_all_pdfs("../data")

    print(f"Loaded {len(documents)} pages")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("../faiss_index")

    print("✅ Ingestion complete!")


if __name__ == "__main__":
    ingest()