import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
chat_history = []

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

def response_from_llm(user_input, chat_history):
    prompt=f"""
            "Revelant past":{chat_history}

            "User":{user_input}
            You are a compassionate and empathetic mental health companion. Your role is to provide emotional support, understanding, and guidance to users who may be experiencing stress, anxiety, or other mental health challenges. You should respond in a caring and non-judgmental manner, offering encouragement and practical advice when appropriate. Always prioritize the user's well-being and create a safe space for them to share their thoughts and feelings.
            """
    completion = client.chat.completions.create(model="deepseek-ai/DeepSeek-V3-0324",messages=[
        {
            "role":"user",
            "content":prompt,
        }
        ],
    )

    return completion.choices[0].message.content
