from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import jwt
from ai_service import generate_lesson, generate_quiz, generate_feedback

load_dotenv()

app = FastAPI(title="EduMentorAI")

# MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET = os.getenv("JWT_SECRET")

@app.get("/test")
def test():
    return {"message": "EduMentorAI Backend Running 🚀"}


@app.get("/ai/lesson")
def ai_lesson(topic: str):
    content = generate_lesson(topic)
    return {"lesson": content}


@app.get("/ai/quiz")
def ai_quiz(topic: str, num_questions: int = 5):
    content = generate_quiz(topic, num_questions)
    return {"quiz": content}


@app.post("/ai/feedback")
def ai_feedback(data: dict):
    text = data.get("text")
    content = generate_feedback(text)
    return {"feedback": content}