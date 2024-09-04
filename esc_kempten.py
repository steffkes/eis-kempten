from icalendar import Calendar, Event, vGeo
from datetime import datetime, timedelta
import pandas as pd
import os

from util import compute_event


cal = Calendar()
cal.add("version", "2.0")
cal.add("prodid", "-//eis-kempten//esc-kempten.de//laufschule")

cancelled_times = [
    # pd.Timestamp("2023-12-28T15:45")
]
times = (
    pd.date_range(
        start="2024-10-05T09:00", end="2025-03-30T09:00", freq="W-SAT"
    ).tolist()
    + pd.date_range(
        start="2024-10-10T15:45", end="2025-03-28T15:45", freq="W-THU"
    ).tolist()
)

for time in times:
    event = compute_event(time, time + timedelta(hours=1), "🦈 Laufschule")
    event.add("status", "CANCELLED" if time in cancelled_times else "CONFIRMED")
    event.add("url", "https://www.esc-kempten.de/laufschule/")
    cal.add_component(event)

os.makedirs("build/esc-kempten/", exist_ok=True)
with open("build/esc-kempten/laufschule.ics", "wb") as file:
    file.write(cal.to_ical())
