"""
CalculatorAgent - Agent Configuration
Simple calculator agent that performs basic arithmetic operations through natural language conversation
"""

from agents import Agent
from tools import add, subtract, multiply, divide, modulo
from guardrails import validate_input_length

agent = Agent(
    name="CalculatorAgent",
    instructions="""You are a helpful calculator assistant. When users ask you to perform calculations, use the appropriate calculator tools (add, subtract, multiply, divide, modulo). Extract numbers from their natural language queries and perform the calculations. Always explain what calculation you're doing and provide the result in a friendly, conversational way.""",
    tools=[
        add,
        subtract,
        multiply,
        divide,
        modulo,
    ],
    input_guardrails=[validate_input_length],
)
