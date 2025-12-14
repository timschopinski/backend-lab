from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"id": 1, "name": "Element 1", "description": "Opis 1"},
    {"id": 2, "name": "Element 2", "description": "Opis 2"}
]


@app.get("/health")
def get_health():
    return {
        "status": "OK",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def add_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "description": item.description
    }
    items.append(new_item)
    return new_item
