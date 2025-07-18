from datetime import datetime
from db.database import SessionLocal
from models.expense import Expense

def run():
     # Creates a new session for interacting with the database
    session = SessionLocal()
    try:
        print("\nAdd New Expense")
        print("----------------")
        
        # Get and validate name
        while True:
            name = input("Name: ").strip()
            if name:
                break
            print("Name cannot be empty")
        
        # Get and validate category
        while True:
            category = input("Category: ").strip()
            if category:
                break
            print("Category cannot be empty")
        
        # Get and validate amount
        while True:
            amount_str = input("Amount: ").strip()
            try:
                amount = float(amount_str)
                if amount > 0:
                    break
                print("Amount must be positive")
            except ValueError:
                print("Please enter a valid number")
        
        # Get and validate date
        while True:
            date_str = input("Date (YYYY-MM-DD): ").strip()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
        
        description = input("Description (optional): ").strip() or None
        
        #Create a new Expense instance with the provided data
        expense = Expense(
            name=name,
            category=category,
            amount=amount,
            date=date,
            description=description
        )

        session.add(expense)
        session.commit()
        print("✅ Expense added successfully!")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()