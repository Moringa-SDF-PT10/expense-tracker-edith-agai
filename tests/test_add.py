import datetime
from models.expense import Expense
from db.database import SessionLocal, engine, base

# Setup: Create tables (only once for tests)
base.metadata.create_all(bind=engine)

def test_add_expense():
    session = SessionLocal()

    # dummy expense
    new_expense = Expense(
        name="Test Coffee",
        category="Food",
        amount=250.0,
        date=datetime.date(2025, 7, 18),
        description="Latte at Artcaffe"
    )

    # Add to the expenses database
    session.add(new_expense)
    session.commit()

    # Fetch from the database
    expense = session.query(Expense).filter_by(name="Test Coffee").first()

    assert expense is not None
    assert expense.category == "Food"
    assert expense.amount == 250.0
    assert expense.description == "Latte at Artcaffe"

    # finalise session
    session.delete(expense)
    session.commit()
    session.close()
