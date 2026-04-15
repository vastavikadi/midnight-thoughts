from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, FinalAnswerTool, tool, load_tool
import datetime
import pytz
import requests
import yaml
from common.common import get_model, load_prompts

yaml_path ="prompts/listener_prompt.yaml"

# Get the model and prompts
model = get_model('Qwen/Qwen2.5-Coder-32B-Instruct')

prompts = load_prompts(yaml_path)

final_answer = FinalAnswerTool()
search_tool = DuckDuckGoSearchTool()

@tool
def get_current_time():
    try:
        tz = pytz.timezone('UTC')
        current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        return f"The current local time in {tz} is: {current_time}"
    except Exception as e:
        return f"An error occurred while fetching the current time: {str(e)}"

agent = CodeAgent(
    model=model,
    tools=[final_answer, search_tool],
    max_steps=6,
    verbosity_level=1,
    planning_interval=None,
    name="Listener_Agent",
    description="Empathic Listener agent",
    prompt_templates=prompts
)