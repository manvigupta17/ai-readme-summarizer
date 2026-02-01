# GitHub Guided Tour Agent

An AI-powered Python application that analyzes a GitHub repository and generates a guided onboarding tour for developers using a Large Language Model (Gemini).

---

## Features

- Fetches README from any public GitHub repository  
- Uses Gemini LLM to generate a structured summary  
- Acts like a senior engineer explaining the project  
- Clean modular architecture (GitHub client, LLM client, agent)  
- Command-line interface  

---

## Project Structure

- github_client.py -> GitHub API logic  
- llm_client.py -> Gemini API logic  
- agent.py -> AI agent orchestration  
- main.py -> CLI entry point  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd ai-guided-tour-agent
```
### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\Activate
```
### 3. Install dependencies
```bash
python -m pip install PyGithub google-genai
```
### 4. Set environment variables
```bash
setx GITHUB_TOKEN "your_github_token"
setx GEMINI_API_KEY "your_gemini_api_key"
```
Restart terminal after this.

## Run the Application

```bash
python main.py
```
Enter:
```bash
psf/requests
```
---

## Example Output
The AI generates:

- One-line project summary
- What the project does
- Who it is for
- Key concepts
- Suggested onboarding steps
  
All in a clean, human-readable format.

---

## Learning Outcomes
This project demonstrates:

- API integration (GitHub + Gemini)
- Prompt engineering
- Modular Python system design
- AI agent architecture
- Secure handling of secrets using environment variables





