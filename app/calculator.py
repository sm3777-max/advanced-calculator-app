# app/calculator.py
from decimal import Decimal
from app.operations import OperationFactory
from app.calculation import Calculation
from app.exceptions import OperationError

class Subject:
    """The base class for a Subject that can be observed."""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, calculation: Calculation):
        for observer in self._observers:
            observer.update(calculation)

class Calculator(Subject):
    """The main calculator class that performs calculations and notifies observers."""
    def __init__(self):
        super().__init__()

    def calculate(self, a: Decimal, b: Decimal, operation_name: str) -> Calculation:
        """Performs a calculation and notifies attached observers."""
        calculation = self._perform_operation(a, b, operation_name)
        self.notify(calculation)
        return calculation

    def _perform_operation(self, a: Decimal, b: Decimal, operation_name: str) -> Calculation:
        """Private method to perform the operation logic."""
        try:
            operation_instance = OperationFactory.get_operation(operation_name)
            result = operation_instance.execute(a, b)
            return Calculation(a, b, operation_name, result)
        except OperationError as e:
            # Correctly indented block to re-raise the custom error
            raise OperationError(f"Error during calculation: {e}") from e