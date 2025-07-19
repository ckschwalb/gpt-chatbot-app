import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# CORS settings (adjust frontend URL for production)
origins = [
    "http://localhost:3000",  # React dev server
    "https://yourusername.github.io",  # Replace with your GitHub username
    "https://yourusername.github.io/gpt-chatbot-app",  # Replace with your repo name
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

class ChatRequest(BaseModel):
    messages: list
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 1024
    temperature: float = 0.7

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        response = client.chat.completions.create(
            model=req.model,
            messages=req.messages,
            max_tokens=req.max_tokens,
            temperature=req.temperature,
        )
        return {"choices": [choice.model_dump() for choice in response.choices]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"status": "ok"}
