# MONGO_URI="mongodb+srv://shubhamiitdev:5KjsIw34uQJyfiUf@cluster1.vdq4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
# JWT_SECRET_KEY="o7neEqQKvf2GT444H9sew9CrvjKMevp8"
# ACCESS_TOKEN_EXPIRE_MINUTES=30
# DB_NAME = "test_app"
# db = "test_app"
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
# client = MongoClient(MONGO_URI)
# db = client["project 0"]
