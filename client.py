# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["/home/mcode/Desktop/LLMs/MCP_Server_tutorial/server.py"],
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent("ollama:llama3.1", tools)
            
            print("Math Agent is ready! Type 'quit' to exit.")
            
            while True:
                # Get user input
                user_question = input("\nEnter your question: ")
                
                if user_question.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                if not user_question.strip():
                    continue
                
                try:
                    # Process the question
                    agent_response = await agent.ainvoke({"messages": user_question})
                    
                    # Extract just the final message content
                    final_message = agent_response["messages"][-1].content
                    print(f"Answer: {final_message}")
                    
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())