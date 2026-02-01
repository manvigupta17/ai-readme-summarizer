import os
from github import Github


def fetch_readme(repo_name: str) -> str:
    """
    Fetch and decode README.md from a GitHub repository.
    """

    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise RuntimeError("GITHUB_TOKEN environment variable not set")

    github = Github(github_token)
    repo = github.get_repo(repo_name)
    readme = repo.get_readme()

    return readme.decoded_content.decode("utf-8")


# Temporary test block
if __name__ == "__main__":
    repo = "psf/requests"
    text = fetch_readme(repo)
    print(text[:500])   # print only first 500 characters
