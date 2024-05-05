from typing import Union
from fastapi import FastAPI
from app.routers.documents import router as document_router

app = FastAPI()

app.include_router(document_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
