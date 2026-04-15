from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

memory_text = []
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = None

def store_memory(text:str):
    global index

    embedding = model.encode([text])

    if index is None:
        dimension = embedding.shape[1]
        index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embedding))
    memory_text.append(text)


def retrieve_memory(query:str, k:int=3):
    if index is None:
        return []
    
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k)

    results = [memory_text[i] for i in I[0] if i < len(memory_text)]
    return results