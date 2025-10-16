from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load the api key to env
load_dotenv()

# create the model
llm = OpenAIChat(id="gpt-4.1-mini")

# add user id
user_id = "user1"

# create a database
db = SqliteDb(db_file="demo.db")

# create the agent
agent = Agent(
    model=llm,
    db=db,
    name="agent_with_memory",
    add_history_to_context=True,
    num_history_runs=5,
    stream=True,
    markdown=True
)

# create sessions
session_transformer = "session_transformer"
session_rag = "session_rag"

# # conversation 1 --> session_id=session_transformer
# agent.print_response("hi, can you tell me about transformer architecture in 100 words, make it simple", session_id=session_transformer)

# agent.print_response("what is self attention. explain in a single paragraph.", session_id=session_transformer)

# agent.print_response("what is this conversation all about?", session_id=session_transformer)


# # conversation 2 --> session_id=session_rag
# agent.print_response("what is the role of RAG in AI. explain in 100 words",session_id=session_rag)

# agent.print_response("What does RAG stands for?",session_id=session_rag)

# agent.print_response("What is this conversation all about?",session_id=session_rag)

agent.print_response(input="can you list down the advantages of RAG you talked about earlier. Only list down from previous chat", session_id=session_rag)

print()
print()

print("============ Tranformer Messages =================")
messages_1 = agent.get_chat_history(session_transformer)

for message in messages_1:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: \n{content}")
        
print("\n\n============ RAG Messages =================")
messages_2 = agent.get_chat_history(session_rag)

for message in messages_2:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role: {role}, Message: \n{content}")
        