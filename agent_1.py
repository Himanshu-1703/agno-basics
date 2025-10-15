from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load keys to environment
load_dotenv()

# define the llm
llm = OpenAIChat(id="gpt-4.1-mini")

# create db to store chat history(sessions)
db = SqliteDb(db_file="agent_history.db")

# build the agent
agent = Agent(
    name="my_agent",
    db=db,
    user_id="user1",
    model=llm,
    markdown=True,
    add_history_to_context=True,
    num_history_runs=5,
    stream=True,
)

# agent.print_response(input="Can you read the summary and tell me 5 imp bullet points out of it", session_id="session_123")

# agent.print_response(input="generate a 100 word summary on the topic: RAG", session_id="session_456")

# agent.print_response(input="what was the topic of this conversation?", session_id="session_456")

print("============= Landscape of Gen AI ================")
chat1_messages = agent.get_chat_history(session_id="session_123")

for message in chat1_messages:
    print(f"Role: {message.role}, Content: {message.content}")
    
    
print("\n============= RAG ================")
chat2_messages = agent.get_chat_history(session_id="session_456")

for message in chat2_messages:
    print(f"Role: {message.role}, Content: {message.content}")