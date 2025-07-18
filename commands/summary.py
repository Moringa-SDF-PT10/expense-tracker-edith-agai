from datetime import datetime
from db.database import SessionLocal
from models.expense import Expense
from tabulate import tabulate

#Provides expense summary functionality including:
# - Total spending calculations
# - Category breakdowns
# - Monthly summaries

def fetch_expenses(session, month=None, category=None):
    query = session.query(Expense)
    
    if month:
        try:
            month_num = datetime.strptime(month, "%B").month
            query = query.filter(Expense.date.like(f"%-{month_num:02d}-%"))
        except ValueError:
            print("Invalid month name. Showing all months.")
    
    if category:
        query = query.filter(Expense.category.ilike(f"%{category}%"))
    
    return query.all()

def summarize_expenses(expenses):
    if not expenses:
        return 0, {}

    total = sum(e.amount for e in expenses)
    category_summary = {}
    for e in expenses:
        category_summary[e.category] = category_summary.get(e.category, 0) + e.amount

    return total, category_summary

def print_summary(total, category_summary):
    if not category_summary:
        print("No expenses found.")
        return

    print(f"\nTotal Spending: KES {total:.2f}\n")
    
    ## Prepare and display category breakdown
    print("By Category:")
    print(tabulate(
        [(cat, f"KES {amt:.2f}", f"{(amt/total)*100:.1f}%") 
         for cat, amt in sorted(category_summary.items(), key=lambda x: -x[1])],
        headers=["Category", "Amount", "Percentage"],
        tablefmt="grid"
    ))

    if len(category_summary) > 1:
        top = max(category_summary.items(), key=lambda x: x[1])
        print(f"\nTop Spending Category: {top[0]} (KES {top[1]:.2f})")

def run():
    session = SessionLocal()
    try:
        print("\nExpense Summary")
        print("---------------")
        month = input("Filter by month (e.g., 'July', leave blank for all): ").strip()
        category = input("Filter by category (leave blank for all): ").strip()

        expenses = fetch_expenses(session, month, category)
        total, category_summary = summarize_expenses(expenses)
        print_summary(total, category_summary)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        session.close()
