from datetime import datetime
from db.database import SessionLocal  
from models.expense import Expense    
from tabulate import tabulate

def run():
        # Create a new database session
    session = SessionLocal()
    try:
        print("\nList Expenses")
        print("--------------")
        
        category = input("Filter by category (leave blank for all): ").strip()
        date_str = input("Filter by date (YYYY-MM-DD, leave blank for all): ").strip()
        
        query = session.query(Expense)
        
        # If user provided a category, filter by it
        if category:
            query = query.filter(Expense.category.ilike(f"%{category}%"))
        
        if date_str:
            try:
                # Format the data for display
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                query = query.filter(Expense.date == date)
            except ValueError:
                print("Invalid date format. Showing all expenses.")
        
        expenses = query.order_by(Expense.date.desc()).all()
        
        if not expenses:
            print("No expenses found.")
            return
        
        table_data = [
            [e.id, e.name, e.category, f"${e.amount:.2f}", 
             e.date.strftime("%Y-%m-%d"), e.description or ""]
            for e in expenses
        ]
        
        # Print the data as a table
        print(tabulate(
            table_data, 
            headers=["ID", "Name", "Category", "Amount", "Date", "Description"],
            tablefmt="grid"
        ))
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        session.close()