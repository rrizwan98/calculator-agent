"""
CalculatorAgent - FastAPI Server
Simple calculator agent that performs basic arithmetic operations through natural language conversation
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import Runner, SQLiteSession
from agents import agent

# Load environment variables
load_dotenv()

# Verify OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")

# Initialize FastAPI app
app = FastAPI(
    title="CalculatorAgent",
    description="Simple calculator agent that performs basic arithmetic operations through natural language conversation",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    session_id: str


class CalculateRequest(BaseModel):
    """Request model for direct calculation endpoint"""
    operation: str  # "add", "subtract", "multiply", "divide", "modulo", "sqrt"
    a: float
    b: float | None = None  # Optional for unary operations like sqrt


class CalculateResponse(BaseModel):
    """Response model for calculation endpoint"""
    operation: str
    a: float
    b: float | None = None
    result: float


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "name": "CalculatorAgent",
        "version": "1.0.0",
        "status": "running",
        "description": "Simple calculator agent with natural language interface",
        "endpoints": {
            "/chat": "Natural language calculator conversation",
            "/calculate": "Direct calculation API",
            "/health": "Health check"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint - send a natural language message and get a response.

    Example: "add 5 and 22" or "what is 10 divided by 2?"

    Args:
        request: ChatRequest containing message and optional session_id

    Returns:
        ChatResponse with the agent's response
    """
    try:
        # Create or retrieve session for conversation memory
        session = SQLiteSession(
            session_id=request.session_id,
            db_path="conversations.db",
        )

        # Run the agent
        result = await Runner.run(
            agent,
            request.message,
            session=session,
        )

        return ChatResponse(
            response=result.final_output,
            session_id=request.session_id,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )


@app.post("/calculate", response_model=CalculateResponse)
async def calculate(request: CalculateRequest):
    """
    Direct calculation endpoint - perform arithmetic operations directly.

    Args:
        request: CalculateRequest with operation type and operands

    Returns:
        CalculateResponse with the result
    """
    try:
        from tools import add, subtract, multiply, divide, modulo, sqrt

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "modulo": modulo,
            "sqrt": sqrt,
        }

        if request.operation not in operations:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid operation. Must be one of: {list(operations.keys())}"
            )

        # Perform calculation
        tool_func = operations[request.operation]

        # Handle unary operations (like sqrt) that only need one argument
        if request.operation == "sqrt":
            result = tool_func(request.a)
        else:
            result = tool_func(request.a, request.b)

        return CalculateResponse(
            operation=request.operation,
            a=request.a,
            b=request.b,
            result=result,
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error performing calculation: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
