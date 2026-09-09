import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("Gen-api-key")
)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain what an LLM is to a beginner."
)

print(response.text)
