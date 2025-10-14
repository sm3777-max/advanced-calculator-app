# tests/test_persistence.py
import pandas as pd
from decimal import Decimal
from app.history import History
from app.saver import AutoSaveObserver
from app.calculation import Calculation

# Dummy calculations for testing
calc1 = Calculation(Decimal('100'), Decimal('50'), 'add', Decimal('150'))
calc2 = Calculation(Decimal('20'), Decimal('5'), 'multiply', Decimal('100'))

def test_save_and_load_history(tmp_path):
    """Tests manually saving and loading the history."""
    # tmp_path creates a temporary directory for the test
    file_path = tmp_path / "history.csv"

    # Test saving
    history_to_save = History()
    history_to_save.add_calculation(calc1)
    history_to_save.add_calculation(calc2)
    history_to_save.save_history(str(file_path))

    # Check if the file was actually created
    assert file_path.exists()

    # Test loading
    history_to_load = History()
    history_to_load.load_history(str(file_path))

    # Check if the loaded history matches the saved one
    assert len(history_to_load.calculations) == 2
    assert history_to_load.calculations[0].result == Decimal('150')
    assert history_to_load.calculations[1].operation == 'multiply'

def test_load_nonexistent_file():
    """Tests that loading a non-existent file is handled gracefully."""
    history = History()
    history.load_history("non_existent_file.csv")
    # No assertion needed, the test passes if no exception is raised

def test_autosave_observer(tmp_path):
    """Tests that the AutoSaveObserver correctly saves the history."""
    file_path = tmp_path / "autosave_history.csv"
    
    history = History()
    history.add_calculation(calc1) # Add one calculation to history

    # Create the observer and manually trigger an update
    saver = AutoSaveObserver(history, str(file_path))
    saver.update(calc1) # The update is triggered by a new calculation

    # Check if the file was created and contains the correct data
    assert file_path.exists()
    df = pd.read_csv(file_path)
    assert len(df) == 1
    assert df.iloc[0]['result'] == 150