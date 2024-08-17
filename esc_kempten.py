from icalendar import Calendar, Event, vGeo
from datetime import datetime, timedelta
import pandas as pd
import os

cal = Calendar()
cal.add("version", "2.0")
cal.add("prodid", "-//eis-kempten//esc-kempten.de//laufschule")

cancelled_times = [
    # pd.Timestamp("2023-12-28T15:45")
]

for time in (
    pd.date_range(
        start="2024-09-28T09:00", end="2025-03-30T09:00", freq="W-SAT"
    ).tolist()
    + pd.date_range(
        start="2024-09-26T15:45", end="2025-03-28T15:45", freq="W-THU"
    ).tolist()
):
    event = Event()
    event.add("summary", "🦈 Laufschule")
    event.add("status", "CANCELLED" if time in cancelled_times else "CONFIRMED")
    event.add("dtstart", time)
    event.add("dtend", time + timedelta(hours=1))
    event.add("dtstamp", datetime.now())
    event.add(
        "location", "Eisstadion Kempten, Memminger Str. 137, 87439 Kempten (Allgäu)"
    )
    event.add("geo", vGeo((47.7445565, 10.3025167)))
    cal.add_component(event)

os.makedirs("build/esc-kempten/", exist_ok=True)
with open("build/esc-kempten/laufschule.ics", "wb") as file:
    file.write(cal.to_ical())
