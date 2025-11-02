from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

# Finn riktig port
PORT = int(os.getenv("PORT", 8080))
print(f"🚀 FastAPI kjører på port {PORT}")

@app.get("/")
def root():
    return {"message": "AI Context Hub backend is running!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)

