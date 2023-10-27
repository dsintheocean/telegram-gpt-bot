import os
import openai
from dotenv import load_dotenv

dotenv_path = 'example/.env'
load_dotenv(dotenv_path)
TOKEN_OPENAI: str = os.getenv('TOKEN_OPENAI')
openai.api_key = TOKEN_OPENAI

def gpt_response(text: str) -> str:
    processed: str = text.lower()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=processed,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        )
    return response.choices[0].text
