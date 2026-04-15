from fastapi import FastAPI
import json
import asyncio
from .llm import response_from_llm
from .schemas import ChatRequest, ChatResponse, APIResponse
from .memory import retrieve_memory, store_memory

app = FastAPI()

@app.get("/input")
async def read_input():
    return APIResponse(message="Welcome to the Mental Companion API! Please send a POST request to /input with your message to receive a response from the chatbot.", status_code=200)

@app.post("/input")
async def create_input(data: ChatRequest):
    store_memory(f"User: {data.input}")
    previous_memories = retrieve_memory(data.input)
    try:
        response = response_from_llm(data.input, previous_memories)
    except Exception as e:
        return APIResponse(message="Error generating response", status_code=500, response=None, error=str(e))
    return APIResponse(message="Response generated successfully", status_code=200, response=ChatResponse(response=response))

