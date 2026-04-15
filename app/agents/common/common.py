from smolagents import ToolCallingAgent, InferenceClientModel, DuckDuckGoSearchTool, FinalAnswerTool,PromptTemplates, tool, load_tool
import datetime
import pytz
import requests
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def get_model(model_id:str):
    model = InferenceClientModel(
    max_tokens=2096,
    temperature=0.5,
    model_id=model_id,
    custom_role_conversions=None,
    )
    return model


def load_prompts(file_path):
    file_path = BASE_DIR / file_path
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            prompts = yaml.safe_load(file)
        prompt_templates = PromptTemplates(
            system_prompt=prompts["prompt"],
            planning={
                "initial_plan": "Break the problem into steps and create a clear plan.",
                "update_plan_pre_messages": "Review previous steps and context before updating the plan.",
                "update_plan_post_messages": "Update the plan based on new observations and remaining steps."
            },

            managed_agent={
                "task": "You are an assistant solving the following task:\n{task}",
                "report": "Here is the final answer from the managed agent:\n{final_answer}"
            },

            final_answer={
                "pre_messages": "You are about to provide the final answer.",
                "post_messages": "Provide a clear, structured, and helpful response to the user."
            }
        )
    except Exception as e:
        print(f"Error loading prompts from {file_path}: {e}")
        prompt_templates = {}
    return prompt_templates