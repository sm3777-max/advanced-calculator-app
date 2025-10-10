# tests/test_commands.py
from app.commands import command, COMMANDS

def test_command_decorator():
    """Tests that the @command decorator registers a function."""
    # Ensure the registry is clean before the test
    COMMANDS.clear()

    # Define a dummy function and apply the decorator
    @command("A test command.")
    def dummy_command():
        pass

    # Check if the command was registered correctly
    assert "dummy_command" in COMMANDS
    assert COMMANDS["dummy_command"] == "A test command."

    # Clean up after the test
    COMMANDS.clear()