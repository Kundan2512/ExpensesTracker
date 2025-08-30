import os
import pandas as pd
from typing import List, Dict

class StoreExpenses:
    def __init__(self):
        # Store file inside current project /datacsv/expenses.csv
        self.EXPENSES_FILE = os.path.join(
            os.path.dirname(__file__), "datacsv", "expenses.csv"
        )
        self.CSV_HEADERS = ["date", "category", "amount", "description"]

    def ensure_files_exist(self):
        """Create CSV with header if not exists"""
        data_dir = os.path.dirname(self.EXPENSES_FILE)
        os.makedirs(data_dir, exist_ok=True)

        if not os.path.exists(self.EXPENSES_FILE):
            # Create empty DataFrame with correct columns
            df = pd.DataFrame(columns=self.CSV_HEADERS)
            df.to_csv(self.EXPENSES_FILE, index=False)

    def load_expenses(self) -> List[Dict]:
        """Load all expenses as a list of dictionaries"""
        self.ensure_files_exist()
        if os.path.exists(self.EXPENSES_FILE) and os.path.getsize(self.EXPENSES_FILE) > 0:
            df = pd.read_csv(self.EXPENSES_FILE)
            return df.to_dict(orient="records")  # DataFrame → list of dicts
        return []

    def save_expenses(self, expenses: List[Dict]) -> None:
        """Overwrite the CSV with a list of expenses (dicts)"""
        self.ensure_files_exist()
        df = pd.DataFrame(expenses, columns=self.CSV_HEADERS)
        df.to_csv(self.EXPENSES_FILE, index=False)

