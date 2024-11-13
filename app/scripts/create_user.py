from pymongo import MongoClient
from app.config import MONGO_URI
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
client = MongoClient(MONGO_URI)
db = client["project0"]
users_collection = db["users"]

def create_user(username: str, email: str, password: str, role: str = "user"):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password, role=role)
    users_collection.insert_one(user.dict(by_alias=True))
    print("User created successfully.")
