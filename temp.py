import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

prompt = "Suggest 3 creative and catchy names for a university coding club."

def run_at_temperature(temp: float) -> str:
    """Invokes the model with a specified decoding temperature."""
    if api_key and api_key != "your_gemini_api_key_here":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        # Configure temperature via generation_config dictionary
        model = genai.GenerativeModel(
            model_name="gemini-3.6-flash",
            generation_config={"temperature": temp}
        )
        # Chained call: invoke -> extract text -> trim whitespace
        return model.generate_content(prompt).text.strip()
    return f"Sample names at temp={temp}: 1. CodeCampus, 2. ByteSociety, 3. DevGuild."

print("Prompt:", prompt)
print("\n" + "=" * 60)
print("1. RUNNING WITH TEMPERATURE = 0.0 (Strict & Deterministic):")
print("=" * 60)
print(run_at_temperature(0.0))

print("\n" + "=" * 60)
print("2. RUNNING WITH TEMPERATURE = 1.0 (Creative & Diverse):")
print("=" * 60)
print(run_at_temperature(1.0))
print("=" * 60)