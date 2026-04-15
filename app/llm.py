import os
from openai import OpenAI

from dotenv import load_dotenv
from .agents.agents import run_agents, synthesize_responses
from .memory import store_memory

load_dotenv()
chat_history = []

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

def response_from_llm(user_input, chat_history):
    listener_response, thinker_response = run_agents(user_input=user_input, memory_context=chat_history)
    final_response = synthesize_responses(listener_response, thinker_response)
    store_memory(f"User: {user_input}\nListener: {listener_response}\nThinker: {thinker_response}\nFinal Response: {final_response}")
    return final_response
    