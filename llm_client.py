import os
from google import genai


def generate_with_llm(prompt: str) -> str:
    """
    Send a prompt to Gemini and return generated text.
    """

    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=gemini_key)

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# Temporary test block
if __name__ == "__main__":
    test_prompt = "Explain what a Large Language Model is in 2 simple sentences."
    result = generate_with_llm(test_prompt)
    print(result)
