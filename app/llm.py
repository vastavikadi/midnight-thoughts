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
    completion = client.chat.completions.create(model="deepseek-ai/DeepSeek-V3-0324",messages=[
        {
            "role":"user",
            "content":user_input,
        }
        ],
    )

    return completion.choices[0].message.content



def generate_response(user_input):
    chat_history.append({"role":"user", "content":user_input})

    response = response_from_llm(user_input, chat_history)
    chat_history.append({"role":"assistant", "content":response})
    return response