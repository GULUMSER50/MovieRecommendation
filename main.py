from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPEN_AI_APIKEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

prompt = input("What kind of Movie are you thinking about?")

# Create a completion
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message)