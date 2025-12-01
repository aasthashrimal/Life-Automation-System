from orchestrator.helpers.google_sheets import fetch_records, add_record
import yaml

with open("settings.yaml") as f:
    settings = yaml.safe_load(f)

SHEET_ID = settings["google_sheets"]["expense_sheet_id"]

class ExpenseAgent:
    def __init__(self):
        self.sheet_id = SHEET_ID

    def handle(self, goal):
        # Example: fetch all expenses
        records = fetch_records(self.sheet_id)
        return records

    def log_expense(self, expense: dict):
        add_record(self.sheet_id, expense)
        return {"status": "success", "expense_logged": expense}
