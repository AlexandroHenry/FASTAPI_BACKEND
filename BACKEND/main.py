from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from domain.user import user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 현재 디렉토리 경로를 가져옴
current_dir = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "../frontend/public")), name="static")

app.include_router(user_router.router)