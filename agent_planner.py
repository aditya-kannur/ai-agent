import requests
import json
from rich.console import Console
import os
from dotenv import load_dotenv
load_dotenv()

console = Console()

# Groq API settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"  # You can try llama3-70b if needed

# Prompt Template
SYSTEM_PROMPT = """
You are a helpful AI agent. The user gives you a goal like "Plan a study schedule for TensorFlow in 3 days".
Break it down into a step-by-step plan with 3 daily tasks. Be clear and actionable.
"""

def query_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()
    return result["choices"][0]["message"]["content"]

def save_to_file(content, filename="study_plan.txt"):
    with open(filename, "w") as f:
        f.write(content)
    console.print(f"✅ Plan saved to [bold green]{filename}[/]")

def run_agent():
    console.print("[bold blue]Welcome to the AI To-Do Agent[/]")
    user_goal = input("Enter your goal (e.g., Plan a study schedule for PyTorch):\n> ")

    console.print("\n🤖 Thinking...\n")
    plan = query_groq(user_goal)

    console.print("[bold green]Here’s your plan:[/]\n")
    console.print(plan)
    save_to_file(plan)

if __name__ == "__main__":
    run_agent()
