from orchestrator.helpers.google_sheets import fetch_records, add_record
import yaml

with open("settings.yaml") as f:
    settings = yaml.safe_load(f)

SHEET_ID = settings["google_sheets"]["wellness_sheet_id"]

class WellnessAgent:
    def __init__(self):
        self.sheet_id = SHEET_ID

    def handle(self, goal):
        # Fetch all wellness entries
        records = fetch_records(self.sheet_id)
        return records

    def log_wellness(self, wellness: dict):
        add_record(self.sheet_id, wellness)
        return {"status": "success", "wellness_logged": wellness}
