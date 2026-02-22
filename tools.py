"""
Calculator Tools for CalculatorAgent
Basic arithmetic operations: addition, subtraction, multiplication, division, modulo, square root, power
"""

from agents import function_tool
import math


@function_tool
def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    result = a + b
    return result


@function_tool
def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Returns:
        Difference (a - b)
    """
    result = a - b
    return result


@function_tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    result = a * b
    return result


@function_tool
def divide(a: float, b: float) -> float:
    """
    Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient (a / b)

    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    result = a / b
    return result


@function_tool
def modulo(a: float, b: float) -> float:
    """
    Get the remainder when dividing first number by second number.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Remainder (a % b)

    Raises:
        ValueError: If b is zero (modulo by zero)
    """
    if b == 0:
        raise ValueError("Cannot perform modulo by zero")

    result = a % b
    return result


@function_tool
def sqrt(a: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        a: Number to find square root of

    Returns:
        Square root of a

    Raises:
        ValueError: If a is negative
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")

    result = math.sqrt(a)
    return result


@function_tool
def power(a: float, b: float) -> float:
    """
    Raise first number to the power of second number.

    Args:
        a: Base number
        b: Exponent

    Returns:
        a raised to the power of b (a^b)
    """
    result = a ** b
    return result
