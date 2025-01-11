import openai
from config.config import OPENAI_API_KEY

def generate_script(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=500
    )
    script = response.choices[0].text.strip()
    return script

if __name__ == "__main__":
    prompt = "Create a video script about the benefits of AI."
    print(generate_script(prompt))
