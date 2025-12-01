import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yaml

# Load settings
with open("settings.yaml") as f:
    settings = yaml.safe_load(f)

# Use service account JSON
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yaml
import json
import streamlit as st

# Load settings
with open("settings.yaml") as f:
    settings = yaml.safe_load(f)

# Use service account JSON
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheets_client():
    json_creds = json.loads(st.secrets["google_sheets"]["service_account_json"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, SCOPE)
    client = gspread.authorize(creds)
    return client

def get_sheet(sheet_key):
    client = get_sheets_client()
    return client.open_by_key(sheet_key).sheet1  # First sheet

# Fetch all records from a sheet
def fetch_records(sheet_key):
    sheet = get_sheet(sheet_key)
    return sheet.get_all_records()

# Add a new record (row) to the sheet
def add_record(sheet_key, record: dict):
    sheet = get_sheet(sheet_key)
    # Append values in the order of headers
    headers = sheet.row_values(1)
    values = [record.get(h, "") for h in headers]
    sheet.append_row(values)


def get_sheet(sheet_key):
    client = get_sheets_client()
    return client.open_by_key(sheet_key).sheet1  # First sheet

# Fetch all records from a sheet
def fetch_records(sheet_key):
    sheet = get_sheet(sheet_key)
    return sheet.get_all_records()

# Add a new record (row) to the sheet
def add_record(sheet_key, record: dict):
    sheet = get_sheet(sheet_key)
    # Append values in the order of headers
    headers = sheet.row_values(1)
    values = [record.get(h, "") for h in headers]
    sheet.append_row(values)
