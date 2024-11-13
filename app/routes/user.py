from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.auth_utils import verify_token
from app.crud.user_crud import create_user, get_user_by_username
from app.models.user import User
from typing import List

router = APIRouter()
users_collection = db["users"]

def get_current_user(token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return token

@router.get("/", response_model=List[User])
async def read_users(current_user: dict = Depends(get_current_user)):
    # Only admins can access this
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    users = list(users_collection.find())
    return users
