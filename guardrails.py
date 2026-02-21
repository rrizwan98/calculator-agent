"""
Input Guardrails for CalculatorAgent
"""

from agents import InputGuardrail, GuardrailFunctionOutput


@InputGuardrail
def validate_input_length(context):
    """
    Validate that user input does not exceed maximum length.
    Prevents potential abuse and excessive token usage.
    """
    max_length = 1000  # Maximum characters for calculator queries

    if len(context.input) > max_length:
        return GuardrailFunctionOutput.reject_content(
            f"Input too long. Maximum {max_length} characters allowed. "
            f"Your input was {len(context.input)} characters. Please shorten your message."
        )

    return GuardrailFunctionOutput.allow()
