# app/commands.py

COMMANDS = {}

def command(description: str):
    """A decorator to register a function as a command."""
    def decorator(func):
        # Register the function name and its description
        COMMANDS[func.__name__] = description
        # Return the original function
        return func
    return decorator