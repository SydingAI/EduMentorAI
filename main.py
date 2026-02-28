import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"message": "EduMentorAI Backend Running 🚀"}

@app.get("/ai/lesson")
async def generate_lesson(topic: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional teacher creating structured lessons."},
                {"role": "user", "content": f"Create a structured lesson about {topic} with introduction, explanation, examples and short quiz."}
            ],
            temperature=0.7,
        )

        lesson = response.choices[0].message.content

        return {"lesson": lesson}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))