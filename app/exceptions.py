# app/exceptions.py
class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""
    pass

class OperationError(CalculatorError):
    """Raised for errors during an operation (e.g., division by zero)."""
    pass

class ValidationError(CalculatorError):
    """Raised for invalid user input."""
    pass