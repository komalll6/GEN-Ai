import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Define the System Instruction (Persona & Boundaries)
ADVISOR_PERSONA = (
    "You are Dr. Rameshwer, an empathetic university academic mentor. "
    "Rules: "
    "1. Always address the student warmly as 'engineering scholar'. "
    "2. Explain technical concepts using simple everyday analogies. "
    "3. Limit your entire response strictly to 2 sentences."
)

user_query = "What is a database index?"
print(f"Student Query: '{user_query}'\n")

if api_key and api_key != "your_gemini_api_key_here":
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    
    # Pass system_instruction directly during model initialization!
    model = genai.GenerativeModel(
        model_name="gemini-3.6-flash",
        system_instruction=ADVISOR_PERSONA,
        generation_config={"temperature": 0.2}
    )
    reply = model.generate_content(user_query).text.strip()
else:
    reply = (
        "Welcome, engineering scholar! Think of a database index like the index at the back of your textbook, "
        "which helps you instantly jump to the exact page without reading the entire book from start to finish."
    )

print("Dr. Rameshwer's Response:")
print(reply)