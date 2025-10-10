# tests/test_operations.py
import pytest
from decimal import Decimal
from app.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation,
    RootOperation,
)
from app.exceptions import OperationError

def test_add_operation():
    op = AddOperation()
    assert op.execute(Decimal('10'), Decimal('5')) == Decimal('15')
    assert op.execute(Decimal('-1'), Decimal('1')) == Decimal('0')

def test_subtract_operation():
    op = SubtractOperation()
    assert op.execute(Decimal('10'), Decimal('5')) == Decimal('5')
    assert op.execute(Decimal('2'), Decimal('3')) == Decimal('-1')

def test_multiply_operation():
    op = MultiplyOperation()
    assert op.execute(Decimal('10'), Decimal('5')) == Decimal('50')
    assert op.execute(Decimal('5'), Decimal('-2')) == Decimal('-10')

def test_divide_operation():
    op = DivideOperation()
    assert op.execute(Decimal('10'), Decimal('2')) == Decimal('5')
    # Test for division by zero
    with pytest.raises(OperationError, match="Cannot divide by zero."):
        op.execute(Decimal('10'), Decimal('0'))

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('2'), Decimal('3'), Decimal('8')),
    (Decimal('10'), Decimal('0'), Decimal('1')),
    (Decimal('4'), Decimal('-2'), Decimal('0.0625')),
    (Decimal('9'), Decimal('0.5'), Decimal('3')),
])
def test_power_operation(a, b, expected):
    op = PowerOperation()
    assert op.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('64'), Decimal('2'), Decimal('8')),  # Square root
    (Decimal('27'), Decimal('3'), Decimal('3')),  # Cube root
    (Decimal('81'), Decimal('4'), Decimal('3')),  # Fourth root
])
def test_root_operation(a, b, expected):
    op = RootOperation()
    assert op.execute(a, b) == expected

def test_root_operation_invalid_input():
    op = RootOperation()
    # Test for even root of a negative number
    with pytest.raises(OperationError, match="Cannot calculate an even root of a negative number."):
        op.execute(Decimal('-4'), Decimal('2'))