from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

# load the api keys
load_dotenv()

# build a db
db = SqliteDb(db_file="session_state_db/shopping.db")

# give a session id and user id
session_id = "2"
user_id = "user_a"

# create a model
llm = OpenAIChat(id="gpt-4.1-mini")

# define a tool that adds items to shopping list
def add_item(session_state: dict, item: str) -> str:
    """Add an item to the shopping list"""
    # lowercase the item
    item = item.lower()
    # fetch the shopping list
    shopping_list = session_state["shopping_list"]
    
    # check if item in list or not
    if item in shopping_list:
        return f"{item} already in shopping list"
    else:
        shopping_list.append(item)
        return f"{item} added to the shopping list"


# define tool to remove item from shopping list
def remove_item(session_state: dict, item: str) -> str:
    """Removes an item from the shopping list for the items i have already purchased"""
    # lowercase the item
    item = item.lower()
    # fetch the shopping list
    shopping_list = session_state["shopping_list"]
    
    # check item in list or not
    if item not in shopping_list:
        f"{item} not in shopping list. Add the item first"
    else:
       # remove the item from shopping list
       shopping_list.remove(item)
       return f"{item} removed from shopping list"
       

# define tool to read items from the list
def list_items(session_state: dict) -> str:
    """List down all the items in shopping list"""
    # check whether shopping list is empty or not
    # fetch the shopping list
    shopping_list = session_state["shopping_list"]
    
    if shopping_list:
        list_of_items = "\n".join([f"- {item}" for item in shopping_list]) ## - Apple - Banana
        return f"The shopping list is: {list_of_items}"
    else:
        return "The shopping list is empty"
    

# define tool to clear the list
def clear_list(session_state: dict) -> str:
    """Clears the shopping list of all items and gives you empty list"""
    shopping_list = session_state["shopping_list"]
    shopping_list.clear()
    return "Cleared the shopping list of all items"
      
        
# create the agent
agent = Agent(
    model=llm,
    name="agent_with_state",
    session_state={"shopping_list": []},
    session_id=session_id,
    instructions="Your job is to manage shopping lists. you start off with an empty list and you can add item to the list, remove item from the list if i have already bought them, list items in the list or clear the list of all items",
    tools=[add_item, remove_item, clear_list, list_items],
    user_id=user_id,
    db=db,
    stream=True,
    markdown=True
)

agent.print_response("Can you tell me what is on the shopping list")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Add milk to the shopping list")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Add eggs and bread to my shopping list")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("I have bought milk and eggs")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("what is on my list?")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Clear everything from the shopping list and add butter and curd to the list")
print(f"The session state is: {agent.get_session_state(session_id)}")

agent.print_response("Remove oranges from the shopping list")
print(f"The session state is: {agent.get_session_state(session_id)}")