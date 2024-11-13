from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.auth_utils import create_access_token, verify_token
# from app.config import db
from app.models.user import User, Token
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_collection = db["users"]

@router.post("/login", response_model=Token)
async def login(username: str, password: str):
    user = get_user_by_username(users_collection, username)
    if user and pwd_context.verify(password, user["hashed_password"]):
        access_token = create_access_token(data={"username": user["username"], "role": user["role"]})
        return {"access_token": access_token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}
