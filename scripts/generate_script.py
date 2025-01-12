import openai
from time import sleep
from config.config import OPENAI_API_KEY
import random

openai.api_key = OPENAI_API_KEY

def generate_script(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # Generic exception handling to cover all error cases
        print(f"An error occurred: {e}")
        return "An error occurred while generating the script."

if __name__ == "__main__":
    script = generate_script("Your prompt here")
    print(script)
