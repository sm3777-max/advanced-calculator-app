# app/logger.py
import logging

class LoggingObserver:
    """An observer that logs calculations to a file."""
    def __init__(self, log_file="calculator.log"):
        # Create a unique logger instance to avoid conflicts in tests
        self.logger = logging.getLogger(f"Logger_{log_file}")
        self.logger.setLevel(logging.INFO)

        # Remove existing handlers to prevent duplicate logs
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        # Create a file handler to write to the specified file
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def update(self, calculation):
        """Receives notification and logs the calculation details."""
        log_message = f"Operation: {calculation.operation}, Operands: ({calculation.a}, {calculation.b}), Result: {calculation.result}"
        self.logger.info(log_message)