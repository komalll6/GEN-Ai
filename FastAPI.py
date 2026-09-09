import os

from dotenv import load_dotenv
from fastapi import FastAPI, Query
from google import genai

load_dotenv()

app = FastAPI(
    title="My First AI API",
    description="FastAPI + Google Gemini"
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash-lite"


@app.get("/")
def home():
    return {
        "message": "AI API is running"
    }


@app.get("/ask")
def ask(
    question: str = Query(
        ...,
        description="Question to ask Gemini"
    )
):
    response = client.models.generate_content(
        model=MODEL,
        contents=question
    )

    return {
        "question": question,
        "answer": response.text
    }