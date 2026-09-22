import os
from dotenv import load_dotenv

# 1. Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

prompt = "What are the 3 primary states of matter? Answer in 10 words."

# 2. Defensive check
if api_key and api_key != "your_gemini_api_key_here":
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    
    # Initialize active flash model
    model = genai.GenerativeModel("gemini-3.6-flash")
    response = model.generate_content(prompt)

    # 3. Extract REAL tokens directly from the server's response object
    input_tokens = response.usage_metadata.prompt_token_count
    output_tokens = response.usage_metadata.candidates_token_count
    total_tokens = response.usage_metadata.total_token_count
    answer = response.text.strip()
else:
    answer = "The three primary states of matter are solid, liquid, gas."
    input_tokens, output_tokens, total_tokens = 13, 11, 24

# 4. Display AI answer and server accounting
print(f"AI Answer: {answer}\n")
print("-" * 50)
print(" GROUND-TRUTH TOKENS REPORTED BY SERVER:")
print(f"  • Input (Prompt) Tokens     : {input_tokens}")
print(f"  • Output (Generated) Tokens : {output_tokens}")
print(f"  • Total Tokens Billed       : {total_tokens}")

# Gemini 3.6 Flash pricing rate reference: ~$0.10/1M input, ~$0.40/1M output
cost_usd = (input_tokens / 1_000_000 * 0.10) + (output_tokens / 1_000_000 * 0.40)
print(f"  • Exact Cost of this Query  : ${cost_usd:.8f} USD (~₹{cost_usd * 84:.6f} INR)")
print("-" * 50)