from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from search import search_tours_semantic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_endpoint(
    query: str = Query("", description="عبارت جستجو"),
    origin: str | None = None,
    destination: str | None = None,
    airline: str | None = None,
    max_price: int | None = None,
    top_k: int | None = None
):
    return search_tours_semantic(
        query=query,
        origin=origin,
        destination=destination,
        airline=airline,
        max_price=max_price,
        top_k=top_k
    )
