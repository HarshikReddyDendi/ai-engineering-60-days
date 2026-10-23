import os
import pathlib
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is missing from your .env file.")
client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role="user"
prompt = "do you know padho with pratyush"
message ={
    "role": role,
    "content": prompt
}
messages = [message]
response = client.chat.completions.create(
    model=model,
    messages=messages
)
print(response.choices[0].message.content)