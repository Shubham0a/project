from bson.objectid import ObjectId
from app.models.user import User
from pymongo.collection import Collection

def get_user_by_username(users_collection: Collection, username: str):
    return users_collection.find_one({"username": username})

def create_user(users_collection: Collection, user: User):
    result = users_collection.insert_one(user.dict(by_alias=True))
    return str(result.inserted_id)


    