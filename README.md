# AI Readme Summarizer

This repository contains a Python script developed as part of the midterm submission.
The project demonstrates how to build an AI-powered pipeline by combining a traditional API with a Large Language Model.

---

## 📌 What This Project Does

- Accepts a GitHub repository name in `owner/repo` format
- Fetches the repository's `README.md` file using the GitHub API
- Sends the README text to a Large Language Model (Gemini)
- Uses prompt engineering to guide the model’s behavior
- Generates a structured, human-readable summary
- Prints the summary to the terminal
- Handles common API and runtime errors gracefully

---

## 🧠 Concepts Covered (Up to Midterm)

- GitHub REST API usage (via PyGithub)
- Secure authentication using environment variables
- Large Language Model (LLM) API integration
- Prompt engineering (instruction-based prompting)
- AI processing pipelines
- Error handling and robustness

---

## ▶️ How to Run

1. Set the required environment variables:
```bash
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key

