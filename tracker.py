import sys
from commands import add, list as list_cmd, summary
from db.database import init_db

def interactive_mode():
    """Run the interactive menu"""
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Summary")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            add.run()
        elif choice == "2":
            list_cmd.run()
        elif choice == "3":
            summary.run()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    # Initialize database if needed
    init_db()
    
    if len(sys.argv) == 1:
        interactive_mode()
    elif sys.argv[1] == "add":
        add.run()
    elif sys.argv[1] == "list":
        list_cmd.run()
    elif sys.argv[1] == "summary":
        summary.run()
    else:
        print("Unknown command. Available commands:")
        print("  python tracker.py        - Interactive mode")
        print("  python tracker.py add    - Add expense")
        print("  python tracker.py list   - List expenses")
        print("  python tracker.py summary - Show summary")