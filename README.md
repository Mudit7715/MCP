# MCP Server with Ollama Integration

A simple **Model Context Protocol (MCP)** server that extends AI capabilities with useful tools for file operations, calculations, text processing, and more. This project demonstrates how to create custom tools that AI models can use through Ollama.

---

## 🎯 What is This?

This project creates a **bridge** between AI models (like those running in Ollama) and your computer's functionality. Think of it as giving the AI hands to:
- Do math calculations
- Check files on your computer
- Transform text
- Generate passwords
- Convert temperatures
- And much more!

---

## 🚀 Features

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

- Python 3.8 or higher
- Ollama installed and running
- Basic familiarity with terminal/command line

---

## 🛠️ Installation

### Step 1: Clone or Download

```bash
# Create project directory
mkdir mcp-ollama-server
cd mcp-ollama-server

# Copy the provided files into this directory

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
pip install langchain-mcp-adapters langgraph langchain-ollama


# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not installed, visit: [https://ollama.ai](https://ollama.com/library)
# Pull a model (if you don't have one)
ollama pull llama3.1
```

### Project Structure
```bash
mcp-ollama-server/
├── server.py          # MCP server with all tools
├── client.py          # Client that connects server to Ollama
├── config.json        # Server configuration
├── mcp_env/           # Virtual environment
└── README.md          # This file
```

### Start the client (automatically starts the server)
```bash
source mcp_env/bin/activate
python server.py

# Open another terminal and the run:
python client.py
```


