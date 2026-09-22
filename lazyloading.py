import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key1 = os.getenv("GEMINI_API_KEY")

prompt = "Explain Artificial Intelligence in one single sentence."
print(f"Prompt: {prompt}\n")

if api_key1 and api_key1 != "your_gemini_api_key_here":
    
    genai.configure(api_key=api_key1)
    
   
    model = genai.GenerativeModel("gemini-3.6-flash")
   
    response = model.generate_content(prompt)
    
   
    print(f"Gemini Answer:\n{response.text.strip()}")
else:

    print("Gemini Answer (Simulation Mode):")
    print("AI is the science of creating machines capable of performing tasks that typically require human intelligence.")