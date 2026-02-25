from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_lesson(topic: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an educational AI assistant."},
            {"role": "user", "content": f"Create a detailed lesson note on: {topic}"}
        ]
    )
    return response.choices[0].message.content


def generate_quiz(topic: str, num_questions: int):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate quizzes for students."},
            {"role": "user", "content": f"Create {num_questions} multiple choice questions on {topic}."}
        ]
    )
    return response.choices[0].message.content


def generate_feedback(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a teacher giving constructive feedback."},
            {"role": "user", "content": f"Give academic feedback on this submission:\n{text}"}
        ]
    )
    return response.choices[0].message.content