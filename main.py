from fastapi import FastAPI
from db.base import db
import uvicorn


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)

