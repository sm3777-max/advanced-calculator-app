# app/history.py
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
        # We need at least two states in the stack to undo (the current and the one before it)
        if len(self._undo_stack) <= 1:
            print("Nothing to undo.")
            return

        # Pop the current state and move it to the redo stack
        self._redo_stack.append(self._undo_stack.pop())
        
        # Restore to the previous state, which is now at the top of the undo stack
        self.restore_from_memento(self._undo_stack[-1])
        print("Last calculation undone.")

    def redo(self):
        """Performs a redo operation."""
        if not self._redo_stack:
            print("Nothing to redo.")
            return

        # Get the memento from the redo stack to restore
        memento_to_restore = self._redo_stack.pop()
        
        # Add this state back to the undo stack
        self._undo_stack.append(memento_to_restore)
        
        # Restore the state from the memento
        self.restore_from_memento(memento_to_restore)
        print("Last calculation redone.")