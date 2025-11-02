from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def root():
    return {"message": "AI Context Hub backend is running!"}

@app.get("/summary")
def summary():
    prompt = "Summarize the purpose of AI Context Hub in two sentences."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"summary": response.choices[0].message.content}
