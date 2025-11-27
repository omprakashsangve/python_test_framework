import os
from openai import OpenAI

# Create OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_code(acceptance_criteria):
    prompt = f"""You're an expert QA Automation Engineer.
Write a pytest-compatible API test case based on the following acceptance criteria:

'{acceptance_criteria}'

Assume the base URL is 'https://jsonplaceholder.typicode.com' and use 'requests'.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" if not using GPT-4
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=600
    )

    return response.choices[0].message.content
