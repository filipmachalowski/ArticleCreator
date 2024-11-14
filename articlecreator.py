import os
from dotenv import load_dotenv  # pip install python-dotenv
from openai import OpenAI  # Assuming `OpenAI` is the client class for API interactions

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is loaded
if not api_key:
    raise ValueError("API key is missing. Please add it to the .env file.")

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)