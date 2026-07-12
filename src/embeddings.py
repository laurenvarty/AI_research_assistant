from sentence_transformers import SentenceTransformer

# Load embedding model once
# This converts text into numerical vectors
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):

    # Extract ONLY the text.
    # The page number is metadata for citations,
    # but the embedding model does not need it.
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