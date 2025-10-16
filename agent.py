from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load keys to environment
load_dotenv()

# define the llm
llm = OpenAIChat(id="gpt-4.1-mini")

# create a database
db = SqliteDb(db_file="chat_history.db")

def add_topic_name(session_state: dict, topic: str) -> str:
    """Add topic name to the state"""
    session_state["topic"].append(topic)
    return f"topic: {topic} added to session state"

def add_word_count(session_state: dict, num_words: str) -> str:
    """Add word count to the state"""
    session_state["word_count"].append(num_words)
    return f"State updated"


# build the agent
agent = Agent(
    name="my_agent",
    model=llm,
    db=db,
    session_id="session_1",
    user_id="user1",
    session_state={"topic": [], "word_count": []},
    tools=[add_topic_name, add_word_count],
    instructions="You are a helpful assistant that can write summaries on various topics. You can use the tools to set the topic and word count for the summary in the session state. Make sure to follow the user's instructions carefully. You have access to tools that can help you manage the session state. Topic: {topic} Word Count: {word_count}",
    add_history_to_context=True,
    num_history_runs=5,
    add_session_state_to_context=True,
    markdown=True,
    stream=True,
)

agent.print_response("Write a 100 word summary on the topic: 'Current Scenario of Gen AI in the world' with a catchy title.")

agent.print_response("What topic are we talking about?")

print("Session State:", agent.get_session_state("session_1"))
