from google import genai
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def safe_gemini_call(prompt):
    for _ in range(2):
        try:
            res = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return res.text.strip()
        except Exception as e:
            print("Retrying...", e)
            time.sleep(3)

    return None