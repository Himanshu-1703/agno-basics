from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# load keys to environment
load_dotenv()

# define the llm
llm = OpenAIChat(id="gpt-4.1-mini")

# define the agent
agent = Agent(
    name="agent_with_memory",
    model=llm,
    stream=True,
    markdown=True,
    add_history_to_context=True,
    num_history_runs=3
)

# chat with the agent
agent.print_response("hi my name is Himanshu")

agent.print_response("Can you tell me my name?")