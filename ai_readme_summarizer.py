import os
from github import Github
from google import genai


def fetch_readme(repo_name: str) -> str:
    """Fetch and decode README.md from a GitHub repository."""
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set")

    github = Github(github_token)
    repo = github.get_repo(repo_name)
    readme = repo.get_readme()

    return readme.decoded_content.decode("utf-8")


def summarize_with_llm(text: str) -> str:
    """Summarize README text using Gemini with prompt engineering."""
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=gemini_key)

    prompt = f"""
You are a technical documentation analyst.

Summarize the following GitHub repository README for a beginner.
Focus on:
- What the project does
- What problem it solves
- Who it is for

Use clear bullet points.

README:
{text}
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def main():
    try:
        repo_name = input("Enter GitHub repository (owner/repo): ")

        readme_text = fetch_readme(repo_name)
        summary = summarize_with_llm(readme_text)

        print("\n===== AI GENERATED SUMMARY =====\n")
        print(summary)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
