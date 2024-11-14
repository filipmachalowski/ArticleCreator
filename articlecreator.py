import os
from dotenv import load_dotenv  # pip install python-dotenv
from openai import OpenAI  # pip install openai

# Load API key from .env file
# Create a .env file without filename that contains OPENAI_API_KEY= "insert-api-key-here"
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is loaded
if not api_key:
    raise ValueError("API key is missing. Please add it to the .env file.")

client = OpenAI()

# Read the content from input.txt
input_file_path = "input.txt"

with open(input_file_path, "r") as file:
    user_input = file.read().strip()  # Read and strip any extra whitespace

# Define the system prompt (set clear instructions for the assistant's behavior)
prompt = (
    "You are a journalist receiving an idea for an article. You create great articles to post on the web "
    "by turning ideas into articles. You use basic HTML markup, and all your content will later be placed "
    "inside <body></body> tags by someone else, so do not use <html>, <body>, or <head> tags. "
    "Do not use any other languages like CSS or JavaScript , but make your article with it tags look modern , and be ready for styling later"
    "Recognize the article title and be sure to use H1 for it"
    "Be sure to not skip any disclaimers or important parts"
    "You are part of a team. In your work, include hints for the image team. "
    "In your article, use <img> tags with src='image_placeholder.jpg' and alt with precise text that describes what should be in the image "
    "so the photo team knows exactly what image to insert there."
)

# Make the API request to generate the article
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": user_input},  # Article idea input
        {"role": "system", "content": prompt},  # Journalist role and HTML instructions
    ],
)

# Check if response is available and write the result to artykul.html
output_file_path = "artykul.html"

try:
    # Write the generated response to artykul.html (overwriting the file each time)
    with open(output_file_path, "w", encoding='utf-8') as output_file:
        output_file.write(
            completion.choices[0].message.content
        )  # Write response to file

    print(f"Article has been written to {output_file_path}")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
