from fastapi import FastAPI

from base import base_func

app = FastAPI()

@app.get("/")
def home():
    return {"message": base_func(9)}