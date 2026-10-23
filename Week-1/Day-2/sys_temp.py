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
prompt = "suggest me brand names for a new startup in the tech industry"
message_system = {
    "role": "system",
    "content": "you are a brand manager who suggests brand names for new startups in the tech industry, in one word, catchy, and easy to remember. you will provide 10 brand name suggestions in a list format."
}
message ={
    "role": role,
    "content": prompt
}
messages = [message_system, message]
#tempertature is 0 by default =safe
response = client.chat.completions.create(
    model=model,
    messages=messages,temperature=2
)
print(response.choices[0].message.content)