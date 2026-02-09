from fastapi import FastAPI, Depends
from app.models import User
from app.database import engine, Base
from app.routers import user, task, auth
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"message": "Welcome to the Task Management API!"}

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(task.router)