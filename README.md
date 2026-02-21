# CalculatorAgent

AI-powered calculator agent with natural language interface built using OpenAI Agents SDK.

## Overview

This is an AI-powered calculator agent that understands natural language queries and performs calculations using custom tools.

## Features

### Calculator Operations
- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)
- **Modulo**: Get the remainder when dividing one number by another
- **Square Root**: Calculate the square root of a number

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

1. Clone the repository:
```bash
git clone https://github.com/rrizwan98/calculator-agent.git
cd calculator-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
```

4. Edit `.env` and add your OpenAI API key:
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

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "add 5 and 22",
    "session_id": "user_123"
  }'
```

**Example queries:**
- "add these numbers 5 and 22"
- "what is 100 minus 45?"
- "multiply 7 by 8"
- "divide 50 by 2"
- "what is 17 modulo 5?"
- "what is the square root of 16?"

### Calculate Endpoint (Direct API)

```bash
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "add",
    "a": 5,
    "b": 22
  }'
```

**Available operations:**
- `add` - Addition
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division
- `modulo` - Modulo (remainder)
- `sqrt` - Square root (only requires parameter `a`)

## File Structure

```
calculator_agent/
├── main.py              # FastAPI server
├── agents.py            # Agent configuration
├── tools.py             # Calculator tools
├── guardrails.py        # Input validation
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker config
├── .env.example         # Environment template
└── README.md            # Documentation
```

## License

This project uses OpenAI Agents SDK.

## Author

rrizwan98
