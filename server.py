from fastmcp import FastMCP
import os
from datetime import datetime
import python_weather

# Create our MCP server - think of this as the main control center
mcp = FastMCP(
    name="My Simple Assistant",
    instructions="A helpful server that can greet people, do math, and check files"
)

# Tool 1: A simple greeting function
@mcp.tool()
def say_hello(name: str) -> str:
    """Says hello to someone by name."""
    return f"Hello, {name}! Nice to meet you!"

# Tool 2: A calculator function  
@mcp.tool()
def calculate(operation: str, a: float, b: float) -> str:
    """Performs basic math operations. Operation can be 'add', 'subtract', 'multiply', or 'divide'."""
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero!"
        result = a / b
    else:
        return "Error: Unknown operation. Use 'add', 'subtract', 'multiply', or 'divide'"
    
    return f"The result of {a} {operation} {b} is {result}"

# Tool 3: Check if a file exists
@mcp.tool()
def check_file(file_path: str) -> str:
    """Checks if a file exists on your computer."""
    if os.path.exists(file_path):
        return f"Yes! The file '{file_path}' exists on your computer."
    else:
        return f"No, the file '{file_path}' was not found."

# Tool 4: Generate random numbers
@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> str:
    """Generates a random number between min_val and max_val (inclusive)."""
    import random
    result = random.randint(min_val, max_val)
    return f"Random number between {min_val} and {max_val}: {result}"

# Tool 5: Text operations
@mcp.tool()
def text_transform(text: str, operation: str) -> str:
    """Transform text. Operations: 'upper', 'lower', 'title', 'reverse', 'length'."""
    if operation == "upper":
        return f"Uppercase: {text.upper()}"
    elif operation == "lower":
        return f"Lowercase: {text.lower()}"
    elif operation == "title":
        return f"Title case: {text.title()}"
    elif operation == "reverse":
        return f"Reversed: {text[::-1]}"
    elif operation == "length":
        return f"Length of '{text}': {len(text)} characters"
    else:
        return "Error: Operation must be 'upper', 'lower', 'title', 'reverse', or 'length'"

# Tool 6: List directory contents
@mcp.tool()
def list_directory(directory_path: str = ".") -> str:
    """Lists files and folders in a directory. Defaults to current directory."""
    try:
        items = os.listdir(directory_path)
        if not items:
            return f"Directory '{directory_path}' is empty."
        
        files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
        folders = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]
        
        result = f"Contents of '{directory_path}':\n"
        if folders:
            result += f"Folders ({len(folders)}): {', '.join(folders)}\n"
        if files:
            result += f"Files ({len(files)}): {', '.join(files)}"
        
        return result
    except FileNotFoundError:
        return f"Error: Directory '{directory_path}' not found."
    except PermissionError:
        return f"Error: Permission denied to access '{directory_path}'."

# Tool 7: Temperature converter
@mcp.tool()
def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> str:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Convert to Celsius first
    if from_unit == "fahrenheit" or from_unit == "f":
        celsius = (temperature - 32) * 5/9
    elif from_unit == "kelvin" or from_unit == "k":
        celsius = temperature - 273.15
    elif from_unit == "celsius" or from_unit == "c":
        celsius = temperature
    else:
        return "Error: from_unit must be 'celsius', 'fahrenheit', or 'kelvin'"
    
    # Convert from Celsius to target unit
    if to_unit == "fahrenheit" or to_unit == "f":
        result = celsius * 9/5 + 32
        unit_symbol = "°F"
    elif to_unit == "kelvin" or to_unit == "k":
        result = celsius + 273.15
        unit_symbol = "K"
    elif to_unit == "celsius" or to_unit == "c":
        result = celsius
        unit_symbol = "°C"
    else:
        return "Error: to_unit must be 'celsius', 'fahrenheit', or 'kelvin'"
    
    return f"{temperature}° {from_unit.title()} = {result:.2f}{unit_symbol}"

# Tool 8: Password generator
@mcp.tool()
def generate_password(length: int = 12, include_symbols: bool = True) -> str:
    """Generate a secure random password."""
    import random
    import string
    
    if length < 4:
        return "Error: Password length must be at least 4 characters."
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if include_symbols else ""
    
    # Ensure at least one character from each required set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    if include_symbols:
        password.append(random.choice(symbols))
    
    # Fill the rest with random characters
    all_chars = lowercase + uppercase + digits + symbols
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    
    return f"Generated password ({length} chars): {''.join(password)}"

# Tool 9: Word count and text statistics
@mcp.tool()
def text_stats(text: str) -> str:
    """Get statistics about a text: word count, character count, etc."""
    if not text.strip():
        return "Error: Please provide some text to analyze."
    
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    sentences = len([s for s in text.split('.') if s.strip()])
    paragraphs = len([p for p in text.split('\n') if p.strip()])
    
    return f"""Text Statistics:
- Characters: {characters} (including spaces)
- Characters: {characters_no_spaces} (excluding spaces)
- Words: {len(words)}
- Sentences: {sentences}
- Paragraphs: {paragraphs}
- Average word length: {sum(len(word) for word in words) / len(words):.1f} characters"""

# Resource: Provide current system information
@mcp.resource("system://info")
def get_system_info() -> dict:
    """Provides basic information about the current time and system."""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "System is running normally"
    }

# This is what runs when you start the server
if __name__ == "__main__":
    print("Starting MCP server with Ollama integration...")
    print("You can now:")
    print("1. Use the MCP tools directly")
    print("2. Chat with Ollama through this server")

    mcp.run(transport= "stdio")  # This starts the server and waits for connections
