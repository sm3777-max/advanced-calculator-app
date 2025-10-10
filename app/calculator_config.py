# app/calculator_config.py
import os
from dotenv import load_dotenv

class Config:
    """A class to manage loading and accessing configuration settings."""
    @staticmethod
    def load():
        """Loads environment variables from a .env file."""
        load_dotenv()

    @staticmethod
    def get(variable_name, default_value=None):
        """Gets a configuration variable's value."""
        return os.getenv(variable_name, default_value)