from fastapi import FastAPI
from app.router import router

app = FastAPI()


app.include_router(router)


@app.get("/")
async def health_check():
    return {"message": "Hello, FastAPI!"}
