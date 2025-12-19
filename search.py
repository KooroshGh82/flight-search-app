from mock_data import MOCK_TOURS
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

for tour in MOCK_TOURS:
    text = f"{tour['origin']} {tour['destination']} {tour['description']} {tour['airline']}"
    tour['embedding'] = model.encode(text)

def search_tours_semantic(
    query: str = "",
    origin: str | None = None,
    destination: str | None = None,
    airline: str | None = None,
    max_price: int | None = None,
    top_k: int | None = None  
):
    results = []
    query_emb = model.encode(query) if query.strip() else None

    for tour in MOCK_TOURS:
        similarity = 0
        if query_emb is not None:
            if 'embedding' not in tour:
                text = f"{tour['origin']} {tour['destination']} {tour['description']} {tour['airline']}"
                tour['embedding'] = model.encode(text)
            tour_emb = tour['embedding']
            similarity = np.dot(query_emb, tour_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(tour_emb))

        if origin and tour["origin"] != origin:
            continue
        if destination and tour["destination"] != destination:
            continue
        if airline and tour["airline"] != airline:
            continue
        if max_price is not None and tour["price"] > max_price:
            continue

        tour_copy = tour.copy()
        tour_copy['similarity'] = float(similarity)
        if 'embedding' in tour_copy:
            del tour_copy['embedding']
        results.append(tour_copy)

    if query_emb is not None:
        results.sort(key=lambda x: (-x['similarity'], x['price']))
    else:
        results.sort(key=lambda x: x['price'])

    for idx, tour in enumerate(results, start=1):
        tour['rank'] = idx

    if top_k is not None:
        return results[:top_k]
    return results
