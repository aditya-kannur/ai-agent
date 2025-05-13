 🧠 Spikra: AI To-Do Agent (Groq + Python)

A simple command-line tool that turns your **goals into actionable plans** using **LLaMA3 on Groq**.

---

## 🚀 Features

- ✅ Converts your goal into a step-by-step plan
- ✍️ Saves the plan to `study_plan.txt`
- ⚡ Powered by **Groq API** and **LLaMA3 model**
- 🧠 Works locally via Python CLI

---

## 📦 Installation

Make sure you have **Python 3.8+** installed.

1. Clone this repository:
   ```
   git clone https://github.com/your-username/ai-agent.git
   cd ai-agent
   ```

2. Create a virtual environment (optional but recommended)

```
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate

```
3. Install dependencies:

```
    pip install requests rich
```

4. Install the Groq Python SDK:
```
    pip install groq
```
🔑 Setup Groq API Key
Sign up at https://console.groq.com

Go to your Groq dashboard → API Keys → Create a key

Add the key to your environment variables:

On macOS/Linux:

```     
    GROQ_API_KEY=your_api_key_here  
```

▶️ How to Run
Run the script from the terminal:

```
    python todo_agent.py

```

Then type your goal, for example:

🎯 Enter your goal: Learn the basics of machine learning in 5 days

You'll get a day-wise plan saved to study_plan.txt.