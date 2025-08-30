import pandas as pd
from validator import validate_date, validate_amount, validate_nonempty
from StoreExpences import StoreExpenses

class Expenses:
    def __init__(self):
        self.store_expenses = StoreExpenses()
        self.expenses = self.store_expenses.load_expenses()

    def addExpense(self):
        print("\nAdd Expense")
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        category = input("Enter category (e.g., Food, Travel): ").strip()
        if not validate_nonempty(category):
            print("Category cannot be empty.")
            return

        amount_str = input("Enter amount: ").strip()
        amount = validate_amount(amount_str)
        if amount is None:
            print("Amount must be a positive number.")
            return

        description = input("Enter description: ").strip()
        if not validate_nonempty(description):
            print("Description cannot be empty.")
            return

        self.expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
        print("Expense added successfully.")

    def getExpenses(self):
        print("\nAll Expenses")
        if not self.expenses:
            print("(No expenses yet)")
            return

        valid_count = 0
        for i, e in enumerate(self.expenses, start=1):
            date = e.get("date")
            category = e.get("category")
            amount = e.get("amount")
            description = e.get("description")

            # Validate before display
            if not (validate_date(str(date)) and validate_nonempty(category) and validate_nonempty(description)):
                continue

            try:
                amt = float(amount)
            except Exception:
                continue

            valid_count += 1
            print(f"{i}.{date}\t\t{category}\t\t{amt:.2f}\t\t{description}")

        if valid_count == 0:
            print("(No valid expenses to show)")


    def trackBudget(self):
        current_budget = validate_amount(input("Enter current budget: ").strip())
        total_spent = 0.0
        for e in self.expenses:
            try:
                total_spent += float(e.get("amount", 0))
            except Exception:
                continue

        print(f"Total recorded expenses: {total_spent:.2f}")

        if total_spent > current_budget:
            print("Warning: You have exceeded your budget!")
        else:
            remaining = current_budget - total_spent
            print(f"You have {remaining:.2f} left for the month.")

    def saveExpenses(self):
        try:
            self.store_expenses.save_expenses(self.expenses)
            print("Expenses saved successfully.")
        except Exception as e:
            print(f"Failed to save expenses. {e}")

