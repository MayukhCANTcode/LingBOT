
import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

print("OPENAI FILE =", openai.__file__)


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_content(prompt):

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
