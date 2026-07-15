# vector_store.py

import faiss
import numpy as np

#makes pdf searchable
def create_vector_store(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index
