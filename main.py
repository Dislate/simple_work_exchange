import uvicorn
from fastapi import FastAPI
from db.base import db
from endpoints import users


app = FastAPI(title="Employment exchange")
app.include_router(router=users.router, prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)

