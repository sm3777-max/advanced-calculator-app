# app/calculator_memento.py
import copy

class CalculatorMemento:
    """A Memento to store a snapshot of the calculation history."""
    def __init__(self, history_state: list):
        # We use deepcopy to ensure the state is a completely independent clone.
        # This prevents accidental changes to the stored state.
        self._state = copy.deepcopy(history_state)

    def get_state(self) -> list:
        """Returns the stored history state."""
        return self._state