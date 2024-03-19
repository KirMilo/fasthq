from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server started")
    yield
    print("Server shoot down")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def main_page():
    return {"message": "Welcome to main page"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)