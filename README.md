# MCP Server with Ollama Integration

A simple **Model Context Protocol (MCP)** server that extends AI capabilities with useful tools for file operations, calculations, text processing, and more. This project demonstrates how to create custom tools that AI models can use through Ollama.

---

## 🎯 What is This?

This is a tutorial which creates a **bridge** between AI models (like those running in Ollama) and your computer's functionality using Model Context Protocol, Langchain and Ollama. Think of it as giving the AI hands to do any task which ealier seem to impossible by AI.

---

## 🚀 Features
This is a very basic implementation on top of which we can build more.(No external APIs connected yet)

### Available Tools

| Tool               | Description                          | Example Usage                         |
|--------------------|--------------------------------------|----------------------------------------|
| **Calculator**      | Basic math operations                | "Calculate 15 + 25"                    |
| **File Checker**    | Check if files exist                 | "Does 'document.txt' exist?"          |
| **Directory Listing** | List folder contents              | "What's in my home folder?"           |
| **Text Transform**  | Change text case, reverse, etc.      | "Make 'hello world' uppercase"        |
| **Temperature Converter** | Convert between °C, °F, K    | "Convert 25°C to Fahrenheit"          |
| **Password Generator** | Generate secure passwords        | "Create a 16-character password"      |
| **Random Numbers**  | Generate random numbers              | "Give me a number between 1-100"      |
| **Text Statistics** | Analyze text (word count, etc.)      | "Analyze this paragraph"              |
| **Greeting**        | Personalized greetings               | "Say hello to Alice"                  |

---

## 📋 Prerequisites

- Python 3.10 or higher
- Ollama installed and running
- Basic familiarity with terminal/command line
- Langchain models
- API basics

---

## 🛠️ Installation

### Step 1: Clone or Download

```bash
# Download files 
wget https://github.com/Mudit7715/MCP.git
cd MCP

# Create virtual environment
python -m venv mcp_env
# Activate it
source mcp_env/bin/activate  # Linux/Mac
# OR
mcp_env\Scripts\activate     # Windows
```

### Step 2: Install ollama and required libraries.
```bash
# Install required packages
pip install fastmcp
pip install langchain-mcp-adapters langgraph langchain-ollama langchain

# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not installed, visit: https://ollama.com/library
# Pull a model (if you don't have one)
ollama pull llama3.1
```

### Project Structure
```bash
mcp-ollama-server/
├── server.py          # MCP server with all tools
├── client.py          # Client that connects server to Ollama
├── config.json        # Server configuration
└── README.md          # This file
```

### Step 3: Running the server and client.
```bash
source mcp_env/bin/activate
python server.py

# Open another terminal and the run:
python client.py
```

### Step 4: Using the tools
```bash
Enter your question: Calculate 50 * 3 + 10
Answer: I will calculate that for you. 50 * 3 + 10 = 160

Enter your question: Check if file 'test.txt' exists in current directory
Answer: The file 'test.txt' was not found in the current directory.

Enter your question: Generate a secure password
Answer: Here is a generated 12-character password: K9#mX2$vB8pQ
```

## 🔧 Configuration
### 🛠️ Modify Server Tools

#### To add new tools, edit server.py:
```bash
@mcp.tool()
def your_new_tool(parameter: str) -> str:
    """Description of what your tool does."""
    # Your tool logic here
    return f"Result: {parameter}"
```

### 🤖 Change Ollama Model

Edit client.py and change the model:
```bash
agent = create_react_agent("ollama:llama3.2", tools)  # Change model here
```

### 🛠️ Server Configuration

Edit config.json to change server parameters:
```bash
{
  "mcpServers": {
    "my-simple-assistant": {
      "command": "python",
      "args": ["/full/path/to/your/server.py"],
      "cwd": "/full/path/to/your/project"
    }
  }
}
```
## 🤝 Contributing

Want to add more tools? Here's how:

```bash
@mcp.tool()
def my_awesome_tool(input_param: str) -> str:
    """What this tool does."""
    # Your logic here
    return f"Result: {input_param}"
```
Test it by asking the AI to use your tool

Update documentation with your new tool
