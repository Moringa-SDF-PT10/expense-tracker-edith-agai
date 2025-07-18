# 🌸 Edith's CLI Personal Expense Tracker ₍˶ᵔ ᵕ ᵔ˶₎💸

Hey there~! 👋 This is my personal expense tracker...
 a command-line Python app I built as part of my Moringa Phase 3 individual project 🧡.

It lets you log your spending, filter by category or date, and get neat summaries so your coins don't disappear without a trace (ง •̀_•́)ง 💰

---

## ✨ Features

✅ Add your daily expenses (name, category, amount, date, description)  
✅ View a list of all your expenses or filter by category/date  
✅ See summaries for your spending — like top category and totals!  
✅ Use it interactively *or* by calling commands directly  
✅ Built with **Python**, **SQLite**, **SQLAlchemy ORM**, and **Pipenv**  
✅ Fully tested with `pytest` to avoid bugs 🐛❌

---

## ⚙️ How to Set It Up

> You only need Python 3.8+ and Pipenv 💫

```bash
# Clone the project
git clone https://github.com/Moringa-SDF-PT10/expense-tracker-edith-agai.git
cd expense-tracker-edith-agai

# Install all the dependencies
pipenv install

# Initialize the database
pipenv run init-db
```

You’ll get a fresh local expense.db ready to start tracking expenses! 🧾

# 💻 How to Use It
## 🎮 Interactive Mode (Main Menu Style)

```bash
pipenv run tracker
```

You’ll see a cute little menu like:
1. Add Expense
2. List Expenses
3. Summary
4. Exit
Use this if you like guided CLI sessions 🐣

## ⚡ Command Mode (Quick + Direct)
Add: pipenv run add-expense
List All: pipenv run list-expenses
Filtered: pipenv run list-expenses → then choose category/date
Summary: pipenv run summary
Filtered Summary: pipenv run summary → input month/category


🌱 Example Usage (Screenshots in the video!)
```bash
Name: Milk Tea
Category: Food
Amount: 150
Date: 2025-07-18
Description: Chatime with friends 🧋
```

## ✨ Summary will look something like this:
```bash

diff

Total Spending: KES 500.00

By Category:
+-----------+------------+-------------+
| Category  | Amount     | Percentage  |
+-----------+------------+-------------+
| Food      | KES 500.00 | 100.0%      |
+-----------+------------+-------------+

Top Spending Category: Food (KES 500.00)
```

## 🧪 Tests
I used pytest to test each command (add, list, summary). Just run:

```bash
pipenv run pytest
```

# 📹 Demo Video
Video file: expense-tracker-demo-edith_agai.mp4

In it, I’ll show:

How to set up the project

Interactive mode walkthrough

Command-based mode usage

Summary breakdowns

Seed data in action!

(っ◔◡◔)っ ♥ Thank you for checking out my work! ♥

# 📁 Project Structure
```bash
EXPENSE-TRACKER-EDITH-ACAI/
├── commands/       # CLI logic (add, list, summary)
├── db/             # Database setup
├── models/         # SQLAlchemy expense model
├── tests/          # Pytest unit tests
├── tracker.py      # CLI entry point
├── init_db.py      # DB setup script
├── Pipfile + lock  # Pipenv files
├── README.md       # You’re here!
└── expense.db      # SQLite DB file (optional)
```

💌 Credits
Made with sleepy eyes, caffeine, and love by
Edith Agai ✨