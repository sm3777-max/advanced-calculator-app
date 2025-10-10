# app/calculation.py
from decimal import Decimal

class Calculation:
    """A class to represent a single calculation and its result."""
    def __init__(self, a: Decimal, b: Decimal, operation: str, result: Decimal):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    def __repr__(self):
        """Provides a developer-friendly string representation of the object."""
        return f"Calculation({self.a}, {self.b}, '{self.operation}') = {self.result}"

    def __eq__(self, other):
        """Overrides the default equality comparison."""
        if not isinstance(other, Calculation):
            # Don't attempt to compare against unrelated types
            return NotImplemented
        return (self.a == other.a and
                self.b == other.b and
                self.operation == other.operation and
                self.result == other.result)