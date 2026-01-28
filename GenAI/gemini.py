from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)

response = gemini.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},     
        {"role": "user", "content": "Explain the theory of relativity in simple terms."}
    ]
)

print(response.choices[0].message.content)