import os
from typing import Any

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, ConfigDict, ValidationError


class Ticket(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = ""
    issue: str = ""
    address: str = ""
    email: str = ""
    phone_number: str = ""


def get_client() -> Groq:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing from your .env file.")
    return Groq(api_key=api_key)


def build_response_format() -> dict[str, Any]:
    schema = Ticket.model_json_schema()
    schema["additionalProperties"] = False
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "customer_ticket",
            "strict": True,
            "schema": schema,
        },
    }


def build_messages(ticket_text: str) -> list[dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "You are an assistant that extracts information from customer support tickets. "
                "Extract only information provided in the ticket. Do not invent or guess missing "
                "information. If a field is missing, return an empty string. Return the fields "
                "required by the JSON schema."
            ),
        },
        {
            "role": "user",
            "content": f"Extract the customer details from this ticket:\n{ticket_text}",
        },
    ]


def extract_ticket(ticket_text: str, model_name: str = "openai/gpt-oss-20b") -> Ticket:
    client = get_client()
    response = client.chat.completions.create(
        model=model_name,
        messages=build_messages(ticket_text),
        response_format=build_response_format(),
        max_tokens=300,
    )

    content = response.choices[0].message.content
    if not content:
        raise ValueError("The model returned an empty response.")

    return Ticket.model_validate_json(content)


def main() -> None:
    ticket_text = """
    Hello, my name is Harshik.
    I have an iPhone which is not working at all.
    My address is Hyd.
    My email is harshik@example.com.
    My phone number is 1234567890.
    """

    try:
        ticket = extract_ticket(ticket_text)
        print("\nCustomer Ticket Extracted Successfully:")
        print(ticket.model_dump_json(indent=2))
    except ValidationError as error:
        print("The response failed Pydantic validation:")
        print(error)
    except Exception as error:
        print(f"An error occurred: {error}")


__all__ = ["Ticket", "build_messages", "build_response_format", "extract_ticket", "main"]
