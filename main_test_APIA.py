from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Introduction to APIs")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

items = {}

@app.get("/")
async def read_root():
    return {"Ashad": "hi"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "item": items.get(item_id)}

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item
        return {"item_id": item_id, "item": item}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully"}