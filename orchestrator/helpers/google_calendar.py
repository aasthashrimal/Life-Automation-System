from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def get_upcoming_events(json_file="service_account.json"):
    creds = Credentials.from_service_account_file(json_file, scopes=[
        "https://www.googleapis.com/auth/calendar.readonly"
    ])
    service = build("calendar", "v3", credentials=creds)
    events_result = service.events().list(calendarId='primary', maxResults=5).execute()
    events = events_result.get("items", [])
    return events
