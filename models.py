from pydantic import BaseModel, EmailStr
from utils import hash_password, verify_password
from config import db
from bson.objectid import ObjectId

# User registration model
class RegisterModel(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str  # student, lecturer, admin, ministry

# MongoDB helpers
def create_user(user_data: dict):
    user_data['password'] = hash_password(user_data['password'])
    result = db.users.insert_one(user_data)
    return str(result.inserted_id)

def find_user_by_email(email: str):
    return db.users.find_one({"email": email})