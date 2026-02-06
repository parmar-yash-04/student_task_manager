from fastapi import FastAPI, Depends
from app.models import User
from app.database import engine, Base
from app.routers import user, task, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)