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
prompt1="hello"
prompt2="my name is jhon"
prompt3="hyderabad" 
prompts =[prompt1,prompt2,prompt3]
for prompt in prompts:
    message ={
        "role": role,
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100
    )
    
    usage=response.usage
    print(f"Prompt: {prompt}---> completion tokens used: {usage.completion_tokens}, prompt tokens used: {usage.prompt_tokens}, total tokens used: {usage.total_tokens} finished response: {response.choices[0].finish_reason}")
 