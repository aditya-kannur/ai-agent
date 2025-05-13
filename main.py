from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"

# FastAPI App
app = FastAPI()

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlanRequest(BaseModel):
    goals: List[str]

class PlanResponse(BaseModel):
    plans: List[str]

def query_groq(prompt: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful planner AI. Break the user goal into a 3-day actionable plan."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-plan", response_model=PlanResponse)
def generate_plan(req: PlanRequest):
    results = []
    for goal in req.goals:
        plan = query_groq(goal)
        results.append(plan)
    return {"plans": results}
