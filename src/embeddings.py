# embeddings.py

from sentence_transformers import SentenceTransformer

# This converts text into numerical vectors
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):

    # Extracts only text, ignoring page numbers
    texts = [
        chunk["text"]
        for chunk in chunks
    ]


    # Convert text chunks into vectors
    embeddings = model.encode(
        texts
    )


    return embeddings
#creates embeddings for the text chunks