from fastapi import FastAPI
from pymongo import MongoClient
from app.config import MONGO_URI
from app.routes import auth, user

app = FastAPI()

client = MongoClient(MONGO_URI)
db = client["your_database_name"]

app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")
