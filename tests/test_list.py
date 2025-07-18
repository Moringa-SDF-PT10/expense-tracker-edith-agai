import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.expense import Expense
from datetime import date
from tabulate import tabulate


# Patch input and print for testing
def test_list_all_expenses(monkeypatch, capsys):
    # Mock input
    monkeypatch.setattr('builtins.input', lambda _: '')

    # Mock database session
    class MockSession:
        def query(self, model):
            assert model == Expense
            return self

        def all(self):
            return [
                Expense(id=1, name="Milk", category="Groceries", amount=250.0, date=date(2025, 7, 18), description=""),
                Expense(id=2, name="Bus", category="Transport", amount=50.0, date=date(2025, 7, 17), description="To class")
            ]

        def close(self):
            pass

    # Temporarily override SessionLocal
    import commands.list 
    commands.list.SessionLocal = lambda: MockSession()

    # Run the function
    commands.list .run()

    # Capture output
    captured = capsys.readouterr()
    output = captured.out

    # Verify that expected output is present
    assert "Milk" in output
    assert "Groceries" in output
    assert "Bus" in output
    assert "Transport" in output
    assert "To class" in output

# 🧪 Test: List expenses filtered by category
def test_list_expenses_by_category(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'Transport')

    class MockSession:
        def query(self, model):
            assert model == Expense
            return self

        def filter_by(self, **kwargs):
            assert kwargs == {'category': 'Transport'}
            class Result:
                def all(self):
                    return [
                        Expense(id=2, name="Bus", category="Transport", amount=50.0, date=date(2025, 7, 3), description="To class")
                    ]
            return Result()

        def close(self):
            pass

    import commands.list
    commands.list.SessionLocal = lambda: MockSession()

    commands.list.run()
    output = capsys.readouterr().out

    assert "Bus" in output
    assert "Milk" not in output
    assert "Transport" in output