# tests/test_config_and_io.py
import os
from app.calculator_config import Config
from app.logger import LoggingObserver
from app.calculation import Calculation
from decimal import Decimal

def test_config_load_and_get(monkeypatch):
    """Tests that the Config class can load and retrieve variables."""
    # Use monkeypatch to fake environment variables
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "test.log")
    monkeypatch.setenv("DUMMY_VARIABLE", "dummy_value")

    # The Config class doesn't need a .env file now; it reads from the patched environment
    assert Config.get("CALCULATOR_LOG_FILE") == "test.log"
    assert Config.get("DUMMY_VARIABLE") == "dummy_value"
    assert Config.get("NON_EXISTENT_VAR", "default") == "default"

def test_logging_observer(tmp_path):
    """Tests that the LoggingObserver writes to a file."""
    # tmp_path is a pytest fixture that provides a temporary directory
    log_file = tmp_path / "test.log"
    
    # Initialize the logger with the temporary file path
    logger = LoggingObserver(str(log_file))
    
    # Create a dummy calculation and notify the logger
    calc = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
    logger.update(calc)

    # Check that the log file was created and contains the correct message
    assert log_file.exists()
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Operation: add" in log_content
        assert "Operands: (10, 5)" in log_content
        assert "Result: 15" in log_content