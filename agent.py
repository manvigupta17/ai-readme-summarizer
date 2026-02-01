from github_client import fetch_readme
from llm_client import generate_with_llm


def generate_guided_tour(repo_name: str) -> str:
    """
    Generate a guided developer tour for a GitHub repository.
    """

    # 1. Get data from GitHub
    readme_text = fetch_readme(repo_name)

    # 2. Build a smart prompt
    prompt = f"""
You are a senior software engineer onboarding a new developer.

The following is the README of a GitHub repository:

{readme_text}

Generate a guided developer tour including:

1. One-line summary of the project
2. What the project does
3. Who this project is for
4. Key concepts a beginner should understand
5. Suggested next steps for onboarding

Use clear sections and bullet points.
"""

    # 3. Send to Gemini
    result = generate_with_llm(prompt)

    return result


# Temporary test block
if __name__ == "__main__":
    repo = "psf/requests"
    tour = generate_guided_tour(repo)
    print(tour)
