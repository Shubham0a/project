from fastapi import FastAPI
from pymongo import MongoClient
from app.config import MONGO_URI
from app.routes import auth, user


app = FastAPI()

client = MongoClient(MONGO_URI)
db = client["user_data"]

# client = MongoClient("mongodb+srv://shubhamiitdev:5KjsIw34uQJyfiUf@cluster1.vdq4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")

@app.get("/")
async def check_connection():
    try:
        client.server_info()  # This will raise an exception if the connection is not successful
        return {"message": "Connected to MongoDB successfully!"}
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to MongoDB: {str(e)}")


app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")
