# app/operations.py
from abc import ABC, abstractmethod
from decimal import Decimal
import math
from app.exceptions import OperationError

class Operation(ABC):
    """The base class for all arithmetic operations."""
    @abstractmethod
    def execute(self, a, b):
        """Executes the arithmetic operation."""
        pass

class AddOperation(Operation):
    def execute(self, a, b):
        return a + b

class SubtractOperation(Operation):
    def execute(self, a, b):
        return a - b

class MultiplyOperation(Operation):
    def execute(self, a, b):
        return a * b

class DivideOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b

class PowerOperation(Operation):
    def execute(self, a, b):
        return a ** b

class RootOperation(Operation):
    def execute(self, a, b):
        # First, check for the invalid case: even root of a negative number
        if a < 0 and b % 2 == 0:
            raise OperationError("Cannot calculate an even root of a negative number.")
        
        # Handle the valid case for odd roots of negative numbers
        if a < 0:
            # Calculate the root of the absolute value, then re-apply the negative sign
            return -(-a) ** (1 / b)
        
        # Handle all positive numbers normally
        return a ** (1 / b)

# --- Added Mandatory Operations ---

class ModulusOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot perform modulus by zero.")
        return a % b

class IntegerDivisionOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot perform integer division by zero.")
        return a // b

class PercentageOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate percentage with a zero denominator.")
        return (a / b) * 100

class AbsoluteDifferenceOperation(Operation):
    def execute(self, a, b):
        return abs(a - b)

# --- End of Added Operations ---

class OperationFactory:
    """A factory for creating operation instances."""
    _operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
        # --- Registering new operations ---
        "modulus": ModulusOperation,
        "int_divide": IntegerDivisionOperation,
        "percent": PercentageOperation,
        "abs_diff": AbsoluteDifferenceOperation,
    }

    @staticmethod
    def get_operation(operation_name: str) -> Operation:
        """
        Returns an instance of the requested operation class.
        Raises an OperationError if the operation is not found.
        """
        op_class = OperationFactory._operations.get(operation_name)
        if not op_class:
            raise OperationError(f"Unknown operation: {operation_name}")
        return op_class()