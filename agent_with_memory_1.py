from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.json import JsonDb
from dotenv import load_dotenv

# load the api key to env
load_dotenv()

# create the model
llm = OpenAIChat(id="gpt-4.1-mini")

# add session id
session_id = "session_1"

# create a database
db = JsonDb(db_path="chat_history_db",
            session_table="session_history")

# create the agent
agent = Agent(
    model=llm,
    db=db,
    name="agent_with_memory",
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=10,
    stream=True,
    markdown=True
)

# # give inputs to the agent
agent.print_response(input="Hi, my name is Himanshu")

# agent.print_response(input="Can you tell me my name?")

agent.print_response(input="tell me a joke that is funny")

agent.print_response(input="generate a paragraph on Gen AI")

agent.print_response(input="Can you tell me my name?")

# print(agent.session_id)

messages = agent.get_chat_history(session_id)

for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: {content}")