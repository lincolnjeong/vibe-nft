from typing import Optional

from fastapi import FastAPI
from os import environ

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "master": environ['MASTER_NAME']}


@app.post("/", status_code=200)
def post_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}