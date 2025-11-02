from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Context Hub backend is running!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/check_key")
def check_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return {"has_key": True, "length": len(api_key)}
    return {"has_key": False}

@app.get("/summary")
def summary():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not found in environment"}

    client = OpenAI(api_key=api_key)
    prompt = "Summarize the purpose of AI Context Hub in two sentences."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"summary": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
