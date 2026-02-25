from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from ai_service import generate_lesson, generate_quiz, generate_feedback

# Load environment variables
load_dotenv()

app = FastAPI(title="EduMentorAI")

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI is not set")

client = MongoClient(MONGO_URI)

# ✅ Explicitly select database (FIX FOR RENDER)
db = client["edumentorai"]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "EduMentorAI is live 🚀"}

@app.get("/test")
def test():
    return {"message": "Backend working perfectly 🔥"}

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