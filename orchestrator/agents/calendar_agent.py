from orchestrator.helpers.google_calendar import get_upcoming_events

class CalendarAgent:
    def handle(self, goal):
        events = get_upcoming_events()
        parsed = []
        for e in events:
            parsed.append({
                "summary": e.get("summary"),
                "start": e["start"].get("dateTime", e["start"].get("date")),
                "end": e["end"].get("dateTime", e["end"].get("date"))
            })
        return {"upcoming_events": parsed}
