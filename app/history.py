# app/history.py
import pandas as pd
from decimal import Decimal
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento

class History:
    """The Caretaker class that manages the history of calculations and mementos."""
    def __init__(self):
        """Initializes the history, creating a memento of the initial empty state."""
        self.calculations = []
        self._undo_stack = [self.create_memento()] # Start with a memento of the empty list
        self._redo_stack = []

    def add_calculation(self, calculation: Calculation):
        """Adds a new calculation to the history and saves a memento."""
        self.calculations.append(calculation)
        self._redo_stack.clear()
        self._undo_stack.append(self.create_memento())

    def create_memento(self) -> CalculatorMemento:
        """Creates a memento of the current calculation list."""
        return CalculatorMemento(self.calculations)

    def restore_from_memento(self, memento: CalculatorMemento):
        """Restores the calculation list from a memento."""
        self.calculations = memento.get_state()

    def undo(self):
        """Performs an undo operation."""
        if len(self._undo_stack) <= 1:
            print("Nothing to undo.")
            return

        self._redo_stack.append(self._undo_stack.pop())
        self.restore_from_memento(self._undo_stack[-1])
        print("Last calculation undone.")

    def redo(self):
        """Performs a redo operation."""
        if not self._redo_stack:
            print("Nothing to redo.")
            return

        memento_to_restore = self._redo_stack.pop()
        self._undo_stack.append(memento_to_restore)
        self.restore_from_memento(memento_to_restore)
        print("Last calculation redone.")

    def save_history(self, file_path: str):
        """Saves the current calculation history to a CSV file."""
        if not self.calculations:
            print("History is empty. Nothing to save.")
            return
        
        history_list = [{
            'operand_a': calc.a, 
            'operand_b': calc.b, 
            'operation': calc.operation, 
            'result': calc.result
        } for calc in self.calculations]
        
        df = pd.DataFrame(history_list)
        df.to_csv(file_path, index=False)
        print(f"History successfully saved to {file_path}")

    def load_history(self, file_path: str):
        """Loads calculation history from a CSV file."""
        try:
            df = pd.read_csv(file_path)
            self.calculations.clear()
            for index, row in df.iterrows():
                calc = Calculation(
                    Decimal(str(row['operand_a'])),
                    Decimal(str(row['operand_b'])),
                    row['operation'],
                    Decimal(str(row['result']))
                )
                self.calculations.append(calc)
            # After loading, save an initial state for undo/redo to work correctly
            self._undo_stack = [self.create_memento()]
            self._redo_stack.clear()
            print(f"History successfully loaded from {file_path}")
        except FileNotFoundError:
            print(f"Error: No history file found at {file_path}")
        except Exception as e:
            print(f"An error occurred while loading history: {e}")