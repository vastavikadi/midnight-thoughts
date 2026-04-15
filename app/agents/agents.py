from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, FinalAnswerTool, tool, load_tool
import datetime
import pytz
from .common.common import get_model, load_prompts

yaml_path_thinker ="prompts/thinker_prompt.yaml"
yaml_path_listener ="prompts/listener_prompt.yaml"
yaml_path_synthesizer ="prompts/synthesizer_prompt.yaml"

model = get_model('Qwen/Qwen2.5-Coder-32B-Instruct')

prompts_thinker = load_prompts(yaml_path_thinker)
prompts_listener = load_prompts(yaml_path_listener)
prompts_synthesizer = load_prompts(yaml_path_synthesizer)

final_answer = FinalAnswerTool()
search_tool = DuckDuckGoSearchTool()

# @tool
# def get_current_time():
#     try:
#         tz = pytz.timezone('UTC')
#         current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
#         return f"The current local time in {tz} is: {current_time}"
#     except Exception as e:
#         return f"An error occurred while fetching the current time: {str(e)}"

thinker_agent = CodeAgent(
    model=model,
    tools=[final_answer, search_tool],
    max_steps=2,
    verbosity_level=1,
    planning_interval=None,
    name="Thinker_Agent",
    description="Logical Reasoning agent",
    prompt_templates=prompts_thinker
)

listener_agent = CodeAgent(
    model=model,
    tools=[final_answer, search_tool],
    max_steps=6,
    verbosity_level=1,
    planning_interval=None,
    name="Listener_Agent",
    description="Empathic Listener agent",
    prompt_templates=prompts_listener
)

synthesizer_agent = CodeAgent(
    model=model,
    tools=[final_answer, search_tool],
    max_steps=6,
    verbosity_level=1,
    planning_interval=None,
    name="Synthesizer_Agent",
    description="Response Synthesizer agent",
    prompt_templates=prompts_synthesizer
)

def run_agents(user_input, memory_context):
    context = "\n".join(memory_context)
    print(f"Context passed to agents:\n{context}")

    listener_output = listener_agent.run(
        f"Context:\n{context}\n\nUser: {user_input}"
    )

    thinker_output = thinker_agent.run(
        f"Context:\n{context}\n\nUser: {user_input}"
    )

    return listener_output, thinker_output

def synthesize_responses(listener_response, thinker_response):
    prompt = f"""
    Merge these two responses into a single, coherent answer that is both logically sound and emotionally supportive.

    Listener's response:
    {listener_response}

    Thinker's response:
    {thinker_response}

    Final Answer: Make sure to maintain the emotional tone of the listener's response while incorporating the logical insights from the thinker's response.
    """
    final_response = synthesizer_agent.run(prompt)
    return final_response