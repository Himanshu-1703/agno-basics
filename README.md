# Agno Basics

A comprehensive learning repository demonstrating the fundamentals of building AI agents using the Agno framework. This repository provides hands-on examples showcasing various agent capabilities including memory management, state persistence, tool integration, and web search functionality.

## Introduction

**Agno Basics** is a practical guide for developers looking to understand and implement AI agents using the Agno framework. The repository contains progressive examples that build from simple agent creation to advanced features like stateful conversations, memory persistence across sessions, and tool-calling capabilities. Each example is designed to be self-contained and demonstrates specific agent functionalities with real-world use cases.

Whether you're building a conversational AI, a task automation system, or exploring agentic workflows, this repository serves as your starting point for mastering Agno's powerful features.

## What This Repository Covers

### 1. **Basic Agent Creation**
- **`main.py`**: Version checking and basic setup
- **`agent.py`**: Complete example of an agent with web search, custom tools, and session state management
- **`agent_with_tools.py`**: Simple agent with DuckDuckGo web search integration

### 2. **Memory Management**
The repository demonstrates three different approaches to implementing agent memory:

#### `agent_with_memory_1.py` - JSON-Based Memory
- Uses JsonDb for storing chat history
- Single session conversation with memory persistence
- Demonstrates basic conversational context retention
- Shows how to retrieve and display chat history

#### `agent_with_memory_2.py` - SQLite-Based Memory
- Implements SqliteDb for more robust storage
- Continues conversations across multiple runs
- Retrieves and references previous interactions
- More scalable than JSON for production use

#### `agent_with_memory_3.py` - Multi-Session Memory
- Manages multiple conversation threads simultaneously
- Demonstrates session isolation (e.g., separate sessions for "transformers" and "RAG" topics)
- Shows how to query specific session histories
- Ideal for applications requiring parallel conversation contexts

### 3. **Session State Management**
Progressive examples showing how to maintain and manipulate session state:

#### `agent_with_state_1.py` - Basic State
- Simple user information storage (name, age)
- Demonstrates state initialization and retrieval
- Shows how agents can access session-specific data

#### `agent_with_state_2.py` - Interactive State
- Shopping list management with add functionality
- Custom tools that modify session state
- Real-time state updates and persistence

#### `agent_with_state_3.py` - Advanced State Operations
- Full CRUD operations on shopping lists
  - Add items (with duplicate checking)
  - Remove items (for purchased goods)
  - List all items
  - Clear the entire list
- Error handling and validation
- Complex state manipulation patterns

#### `agent_with_state_4.py` - Multiple State Sessions
- Managing different lists simultaneously (fruits list, dairy list)
- Session isolation with independent state objects
- Demonstrates multi-user or multi-context scenarios
- Advanced session state patterns for real-world applications

### 4. **Tool Integration**
Examples include:
- **Web Search**: DuckDuckGo integration for real-time information retrieval
- **Custom Tools**: Function calling with session state manipulation
- **Tool Composition**: Combining multiple tools in a single agent

### 5. **Database Integration**
- **JsonDb**: Lightweight JSON-based storage for development
- **SqliteDb**: Production-ready SQLite integration for chat history and session states

## Key Features Demonstrated

### Memory & Persistence
- Chat history storage and retrieval
- Session-based conversation management
- Multi-session parallel conversations
- Configurable history context length (`num_history_runs`)

### Session State
- Persistent state across conversations
- State-aware tool execution
- Dynamic state updates
- Session isolation and management

### Tool Calling
- Custom function tools with type hints
- Tool descriptions for LLM understanding
- Session state integration in tools
- Web search capabilities

### Agent Configuration
- Custom instructions and personas
- Streaming responses
- Markdown formatting
- History context control
- User and session identification

## Technology Stack

- **Python**: 3.13+
- **Agno**: 2.1.4+ (AI agent framework)
- **OpenAI**: 2.3.0+ (LLM provider)
- **SQLAlchemy**: 2.0.44+ (Database ORM)
- **DuckDuckGo Search**: 9.6.1+ (Web search tool)
- **python-dotenv**: 1.1.1+ (Environment variable management)

## Prerequisites

- Python 3.13 or higher
- OpenAI API key
- Basic understanding of Python and async programming
- Familiarity with LLM concepts

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Himanshu-1703/agno-basics.git
   cd agno-basics
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install agno>=2.1.4 ddgs>=9.6.1 openai>=2.3.0 python-dotenv>=1.1.1 sqlalchemy>=2.0.44
   ```
   
   Or if using uv:
   ```bash
   uv sync
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Each script can be run independently to demonstrate specific features:

```bash
# Basic agent with tools
python agent_with_tools.py

# Memory examples
python agent_with_memory_1.py
python agent_with_memory_2.py
python agent_with_memory_3.py

# State management examples
python agent_with_state_1.py
python agent_with_state_2.py
python agent_with_state_3.py
python agent_with_state_4.py

# Complete example with all features
python agent.py
```

## Example Output

The agents in this repository can:
- Answer questions with web-searched information
- Remember previous conversations across sessions
- Maintain shopping lists with add/remove/clear operations
- Generate summaries with key points extraction
- Manage multiple conversation contexts simultaneously
- Persist data across runs using databases

## Database Files

The repository includes several database files for state and history persistence:
- `chat_history.db`: Main chat history storage
- `demo.db`: Demo session storage
- `chat_history_db/`: JSON-based history storage
- `session_state_db/`: Session state persistence

## Learning Path

**Recommended order for learning:**
1. Start with `agent_with_tools.py` to understand basic agent creation
2. Progress through `agent_with_memory_1.py` → `agent_with_memory_3.py` for memory concepts
3. Explore state management from `agent_with_state_1.py` → `agent_with_state_4.py`
4. Review `agent.py` to see all concepts combined

## Common Use Cases

- **Customer Support Bots**: Memory-enabled agents that remember customer context
- **Task Management**: Shopping lists, to-do lists with state persistence
- **Research Assistants**: Web search with summary generation and key point extraction
- **Multi-tenant Applications**: Session isolation for different users/contexts
- **Conversational Analytics**: Chat history retrieval and analysis

## Contributing

Contributions are welcome! Feel free to:
- Add new examples demonstrating Agno features
- Improve documentation
- Report issues or bugs
- Suggest enhancements

## License

This project is open-source and available for learning purposes.

## Resources

- [Agno Documentation](https://docs.agno.ai)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [DuckDuckGo Search](https://pypi.org/project/ddgs/)

## Author

**Himanshu**
- GitHub: [@Himanshu-1703](https://github.com/Himanshu-1703)

---

**Note**: Make sure to keep your API keys secure and never commit them to version control. Always use environment variables for sensitive information.
