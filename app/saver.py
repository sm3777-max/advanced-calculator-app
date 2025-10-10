# app/saver.py
import pandas as pd

class AutoSaveObserver:
    """An observer that auto-saves the calculation history to a CSV file."""
    def __init__(self, history_instance, file_path="history.csv"):
        self.history = history_instance
        self.file_path = file_path

    def update(self, calculation):
        """Receives notification and saves the entire history."""
        # Convert the list of Calculation objects to a list of dictionaries
        history_list = [{
            'operation': calc.operation,
            'operand_a': calc.a,
            'operand_b': calc.b,
            'result': calc.result
        } for calc in self.history.calculations]
        
        # Create a pandas DataFrame and save it to CSV
        df = pd.DataFrame(history_list)
        df.to_csv(self.file_path, index=False)
        print(f"History auto-saved to {self.file_path}")