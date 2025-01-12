import openai
from time import sleep
from config.config import OPENAI_API_KEY
import random

openai.api_key = OPENAI_API_KEY

def generate_script(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
        sleep(random.uniform(1, 5))  # Wait between 1 to 5 seconds
        return generate_script(prompt)
    except openai.error.OpenAIError as e:
        print(f"An OpenAI error occurred: {e}")
        return "An OpenAI error occurred while generating the script."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while generating the script."

if __name__ == "__main__":
    script = generate_script("Your prompt here")
    print(script)
