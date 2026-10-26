# Day 4: JSON + Pydantic structured outputs

This project demonstrates how to use Groq's structured output feature with a Pydantic schema to reliably extract customer support details from free-form text.

## What it does

- Defines a `Ticket` model with strongly typed fields
- Builds a JSON schema for Groq structured responses
- Sends a customer ticket to the model
- Validates the returned JSON with Pydantic before printing it

## Setup

1. Create a `.env` file in this directory or parent directory with:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Run the example:

   ```bash
   python Json_pydantic.py
   ```

   or:

   ```bash
   uv run day-4
   ```
