from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load keys to environment
load_dotenv()

# define the llm
llm = OpenAIChat(id="gpt-4.1-mini")

# build the db
db = SqliteDb(db_file="demo.db")

# add custom session id and user id
session_id = "session_2"
user_id = "himanshu"

# define the agent
agent = Agent(
    name="agent_with_memory",
    db=db,
    model=llm,
    session_id=session_id,
    user_id=user_id,
    stream=True,
    markdown=True,
    add_history_to_context=True,
    num_history_runs=3
)

# chat with the agent
agent.print_response("hi my name is Himanshu")

agent.print_response("Can you tell me my name?")

messages = agent.get_chat_history(session_id=session_id)

for message in messages:
    print(f"Role: {message.role}, Content: {message.content}")