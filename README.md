# CalculatorAgent

Simple calculator agent that performs basic arithmetic operations through natural language conversation

## Overview

This is an AI-powered calculator agent built with the OpenAI Agents SDK. It understands natural language queries and performs calculations using custom tools.

## Features

### Calculator Operations
- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)
- **Modulo**: Get the remainder when dividing one number by another
- **Square Root**: Calculate the square root of a number
- **Power**: Raise a number to the power of another (a^b)
- **Absolute**: Get the absolute value of a number (|a|)

### Capabilities
- Natural language understanding (e.g., "add 5 and 22", "what is 10 divided by 2?")
- Conversation memory (remembers previous calculations in a session)
- Two API endpoints: conversational chat and direct calculation
- Input validation and guardrails
- FastAPI server with automatic documentation

## Quick Start

### Prerequisites
- Python 3.11 or higher
- OpenAI API key

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
```

3. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

### Running Locally

```bash
python main.py
```

The server will start on `http://localhost:8000`

### Running with Docker

1. Build the image:
```bash
docker build -t calculator-agent .
```

2. Run the container:
```bash
docker run -p 8000:8000 --env-file .env calculator-agent
```

## API Usage

### Interactive Documentation

Visit `http://localhost:8000/docs` for Swagger UI with interactive API documentation.

### Chat Endpoint (Natural Language)

Send natural language queries to the agent:

```bash
curl -X POST http://localhost:8000/chat \\
  -H "Content-Type: application/json" \\
  -d '{
    "message": "add 5 and 22",
    "session_id": "user_123"
  }'
```

Response:
```json
{
  "response": "I'll add those numbers for you. 5 + 22 = 27",
  "session_id": "user_123"
}
```

**Example queries:**
- "add these numbers 5 and 22"
- "what is 100 minus 45?"
- "multiply 7 by 8"
- "divide 50 by 2"
- "what's 15.5 plus 20.3?"
- "what is 17 modulo 5?" or "get remainder of 20 divided by 3"
- "what is the square root of 16?" or "calculate sqrt of 25"
- "what is 2 to the power of 8?" or "calculate 3 raised to 4"
- "what is the absolute value of -5?" or "calculate |−10|"

### Calculate Endpoint (Direct API)

Perform calculations directly without natural language:

```bash
curl -X POST http://localhost:8000/calculate \\
  -H "Content-Type: application/json" \\
  -d '{
    "operation": "add",
    "a": 5,
    "b": 22
  }'
```

Response:
```json
{
  "operation": "add",
  "a": 5,
  "b": 22,
  "result": 27
}
```

**Available operations:**
- `add` - Addition
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division
- `modulo` - Modulo (remainder)
- `sqrt` - Square root (only requires parameter `a`)
- `power` - Power/Exponentiation (a^b)
- `absolute` - Absolute value (only requires parameter `a`)

### Health Check

```bash
curl http://localhost:8000/health
```

## File Structure

```
calculator_agent/
├── main.py              # FastAPI server with chat and calculate endpoints
├── agents.py            # Agent configuration
├── tools.py             # Calculator tool implementations
├── guardrails.py        # Input validation
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .env.example         # Environment template
└── README.md            # This file
```

## How It Works

1. **Natural Language Processing**: The agent uses OpenAI's language model to understand user queries
2. **Tool Calling**: When a calculation is needed, the agent automatically calls the appropriate calculator tool (add, subtract, multiply, divide)
3. **Result Generation**: The agent formats the result in a friendly, conversational way
4. **Memory**: Conversation history is stored in SQLite, allowing follow-up queries

## Examples

### Natural Language Queries

```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={
        "message": "I need to add 15 and 37",
        "session_id": "session_1"
    }
)
print(response.json()["response"])
# Output: "I'll add those numbers for you. 15 + 37 = 52"
```

### Direct Calculation

```python
import requests

response = requests.post(
    "http://localhost:8000/calculate",
    json={
        "operation": "multiply",
        "a": 12,
        "b": 8
    }
)
print(response.json()["result"])
# Output: 96
```

### Using Session Memory

```python
# First message
requests.post("http://localhost:8000/chat", json={
    "message": "add 10 and 20",
    "session_id": "user_1"
})
# Response: "10 + 20 = 30"

# Follow-up (same session)
requests.post("http://localhost:8000/chat", json={
    "message": "now multiply that by 2",
    "session_id": "user_1"
})
# Agent remembers previous result
```

## Customization

### Modify Calculator Tools

Edit `tools.py` to add new operations:

```python
@function_tool
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent
```

Then add to agent in `agents.py`:

```python
from tools import add, subtract, multiply, divide, power

agent = Agent(
    name="CalculatorAgent",
    tools=[add, subtract, multiply, divide, power],
    ...
)
```

### Adjust Input Limits

Edit `guardrails.py` to change the maximum input length:

```python
max_length = 2000  # Increase to 2000 characters
```

### Change Agent Personality

Edit `agents.py` to modify how the agent responds:

```python
instructions="""You are a fun and enthusiastic calculator assistant!
Use emojis and make math exciting! 🧮✨"""
```

## Troubleshooting

### "OPENAI_API_KEY environment variable is required"
Make sure you've created a `.env` file with your API key.

### Division by zero error
The agent will catch this and return a friendly error message. The `/calculate` endpoint will return a 400 error.

### Large numbers
The calculator supports floats, so very large numbers or many decimal places are supported.

## Development

### Running Tests

```bash
# Install dev dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

## License

This project is generated using OpenAI Agents SDK.

## Support

For issues or questions:
- Check the [OpenAI Agents SDK Documentation](https://platform.openai.com/docs/agents)
- Review error logs in the console
- Verify your API key is set correctly
