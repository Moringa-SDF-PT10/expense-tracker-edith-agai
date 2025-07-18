import pytest
from models.expense import Expense
from commands.summary import summarize_expenses

@pytest.fixture
def mock_expenses():
    return [
        Expense(amount=100, category='Food', date='2025-07-10'),
        Expense(amount=50, category='Transport', date='2025-07-12'),
        Expense(amount=150, category='Food', date='2025-07-15')
    ]

def test_summarize_expenses(mock_expenses):
    total, summary = summarize_expenses(mock_expenses)
    assert total == 300
    assert summary['Food'] == 250
    assert summary['Transport'] == 50
    assert round((summary['Food']/total)*100, 1) == 83.3
