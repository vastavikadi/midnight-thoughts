from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, FinalAnswerTool, tool, load_tool
import datetime
import pytz
import requests
import yaml
import os
from common.common import get_model, load_prompts

yaml_path ="prompts/thinker_prompt.yaml"

model = get_model('Qwen/Qwen2.5-Coder-32B-Instruct')

prompts = load_prompts(yaml_path)

final_answer = FinalAnswerTool()
search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    model=model,
    tools=[final_answer, search_tool],
    max_steps=2,
    verbosity_level=1,
    planning_interval=None,
    name="Thinker_Agent",
    description="Logical Reasoning agent",
    prompt_templates=prompts
)

response = agent.run("I am confused about my career.")
print(response)