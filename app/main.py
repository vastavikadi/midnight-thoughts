from fastapi import FastAPI
import json
import asyncio
from .llm import generate_response
from .schemas import ChatRequest, ChatResponse, APIResponse

app = FastAPI()

@app.get("/input")
async def read_input():
    return APIResponse(message="Welcome to the Mental Companion API! Please send a POST request to /input with your message to receive a response from the chatbot.", status_code=200)

@app.post("/input")
async def create_input(data: ChatRequest):
    try:
        response = generate_response(data.input)
    except Exception as e:
        return APIResponse(message="Error generating response", status_code=500, response=None, error=str(e))
    return APIResponse(message="Response generated successfully", status_code=200, response=ChatResponse(response=response))

