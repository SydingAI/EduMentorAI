from fastapi import APIRouter, HTTPException, Depends
from models import RegisterModel, create_user, find_user_by_email
from utils import verify_password
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# JWT Token creation
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Register
@router.post("/register")
def register(user: RegisterModel):
    if find_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = create_user(user.dict())
    return {"id": user_id, "message": "User registered successfully"}

# Login
@router.post("/login")
def login(data: dict):
    user = find_user_by_email(data['email'])
    if not user or not verify_password(data['password'], user['password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user['email'], "role": user['role']})
    return {"access_token": token, "token_type": "bearer"}