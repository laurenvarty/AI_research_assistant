# retrieval.py

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

#retrieves asked for chunks of text from the pdf
def retrieve(query, index, chunks, k=4):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = [chunks[i] for i in indices[0]]

    return results
