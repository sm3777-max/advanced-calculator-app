# tests/test_history.py
from decimal import Decimal
from app.history import History
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento

# Create some dummy calculation instances to use in tests
calc1 = Calculation(Decimal('10'), Decimal('5'), 'add', Decimal('15'))
calc2 = Calculation(Decimal('15'), Decimal('2'), 'multiply', Decimal('30'))
calc3 = Calculation(Decimal('30'), Decimal('10'), 'subtract', Decimal('20'))

def test_history_add():
    history = History()
    assert len(history.calculations) == 0
    history.add_calculation(calc1)
    assert len(history.calculations) == 1
    assert history.calculations[0] == calc1

def test_history_undo():
    history = History()
    history.add_calculation(calc1)
    history.add_calculation(calc2)
    
    assert len(history.calculations) == 2
    
    # First undo
    history.undo()
    assert len(history.calculations) == 1
    assert history.calculations[-1] == calc1

    # Second undo
    history.undo()
    assert len(history.calculations) == 0
    
    # Undo on empty history
    history.undo() # Should print a message and do nothing
    assert len(history.calculations) == 0

def test_history_redo():
    history = History()
    history.add_calculation(calc1)
    history.add_calculation(calc2)

    # Undo twice to populate redo stack
    history.undo()
    history.undo()
    assert len(history.calculations) == 0

    # First redo
    history.redo()
    assert len(history.calculations) == 1
    assert history.calculations[-1] == calc1

    # Second redo
    history.redo()
    assert len(history.calculations) == 2
    assert history.calculations[-1] == calc2

    # Redo with nothing to redo
    history.redo() # Should print and do nothing
    assert len(history.calculations) == 2

def test_new_action_clears_redo_stack():
    history = History()
    history.add_calculation(calc1)
    history.add_calculation(calc2)
    
    history.undo() # History is now [calc1]
    assert len(history._redo_stack) == 1 # Redo stack has a memento for [calc1, calc2]
    
    # Perform a new action
    history.add_calculation(calc3) # History is now [calc1, calc3]
    
    # The redo stack should be cleared
    assert len(history._redo_stack) == 0
    
    # Trying to redo should do nothing
    history.redo()
    assert len(history.calculations) == 2
    assert history.calculations[-1] == calc3