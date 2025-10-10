# tests/test_calculator.py
import pytest
from decimal import Decimal
from app.calculator import Calculator
from app.exceptions import OperationError

class MockObserver:
    """A mock observer to test the notification system."""
    def __init__(self):
        self.notified = False
        self.calculation = None

    def update(self, calculation):
        self.notified = True
        self.calculation = calculation

def test_calculator_operations():
    calc = Calculator()
    # Test a few standard operations to ensure the factory and execution work
    assert calc.calculate(Decimal('10'), Decimal('5'), 'add').result == Decimal('15')
    assert calc.calculate(Decimal('10'), Decimal('2'), 'multiply').result == Decimal('20')
    assert calc.calculate(Decimal('3'), Decimal('4'), 'power').result == Decimal('81')

def test_calculator_unknown_operation_raises_error():
    calc = Calculator()
    with pytest.raises(OperationError, match="Unknown operation: unknown"):
        calc.calculate(Decimal('10'), Decimal('5'), 'unknown')

def test_calculator_division_by_zero_error():
    calc = Calculator()
    with pytest.raises(OperationError, match="Cannot divide by zero."):
        calc.calculate(Decimal('10'), Decimal('0'), 'divide')

def test_calculator_notifies_observers():
    calc = Calculator()
    observer = MockObserver()
    calc.attach(observer)

    # Perform a calculation
    calc.calculate(Decimal('20'), Decimal('4'), 'divide')

    # Check that the observer was notified
    assert observer.notified is True
    assert observer.calculation.result == Decimal('5')

    # Detach the observer and test again
    calc.detach(observer)
    observer.notified = False # Reset the flag
    
    calc.calculate(Decimal('10'), Decimal('2'), 'add')
    assert observer.notified is False # Should not have been notified