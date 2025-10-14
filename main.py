# main.py
from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.history import History
from app.logger import LoggingObserver
from app.saver import AutoSaveObserver
from app.calculator_config import Config
from app.exceptions import ValidationError
from app.commands import command, COMMANDS

class App:
    def __init__(self):
        Config.load()
        self.calculator = Calculator()
        self.history_manager = History()

        log_file = Config.get("CALCULATOR_LOG_FILE", "calculator.log")
        history_file = Config.get("CALCULATOR_HISTORY_FILE", "history.csv")
        
        log_observer = LoggingObserver(log_file)
        save_observer = AutoSaveObserver(self.history_manager, history_file)
        self.calculator.attach(log_observer)
        self.calculator.attach(save_observer)

    @command("Displays this help message.")
    def help(self):
        print("Available commands:")
        for name, desc in COMMANDS.items():
            print(f"  {name}: {desc}")

    @command("Shows the calculation history.")
    def history(self):
        if not self.history_manager.calculations:
            print("History is empty.")
        for calc in self.history_manager.calculations:
            print(calc)

    @command("Undoes the last calculation.")
    def undo(self):
        self.history_manager.undo()

    @command("Redoes the last undone calculation.")
    def redo(self):
        self.history_manager.redo()

    @command("Saves the current history to the configured CSV file.")
    def save(self):
        history_file = Config.get("CALCULATOR_HISTORY_FILE", "history.csv")
        self.history_manager.save_history(history_file)

    @command("Loads history from the configured CSV file.")
    def load(self):
        history_file = Config.get("CALCULATOR_HISTORY_FILE", "history.csv")
        self.history_manager.load_history(history_file)

    def start(self):
        print("Welcome to the Advanced Calculator!")
        self.help()

        while True:
            try:
                command_input = input(">>> ").strip().lower()
                if not command_input:
                    continue

                parts = command_input.split()
                cmd_name = parts[0]
                args = parts[1:]

                if cmd_name == "exit":
                    print("Exiting. Goodbye!")
                    break

                if cmd_name in COMMANDS:
                    cmd_method = getattr(self, cmd_name)
                    cmd_method(*args)
                else:
                    if len(parts) != 3:
                        raise ValidationError("Invalid command format. Use: <operation> <a> <b>")
                    
                    op_name, val_a, val_b = parts
                    a, b = Decimal(val_a), Decimal(val_b)
                    
                    calculation = self.calculator.calculate(a, b, op_name)
                    self.history_manager.add_calculation(calculation)
                    print(f"Result: {calculation.result}")

            except (ValidationError, InvalidOperation) as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app = App()
    app.start()