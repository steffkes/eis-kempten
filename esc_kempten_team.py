from icalendar import Calendar, Event, vGeo, vCalAddress, vText
from functools import reduce
from datetime import datetime, timedelta
import dateparser
import requests
import pandas as pd
import os
import re

participationMap = {"c_no___": "DECLINED", "a_yes__": "ACCEPTED"}
iconMap = {"DECLINED": "❌", "ACCEPTED": "✔️", "TENTATIVE": "❔"}


def transformer(state, item):
    (reply, name, date) = item
    date = dateparser.parse(date, settings={"TIMEZONE": "Europe/Berlin"}).isoformat()

    if date not in state:
        state[date] = {}

    state[date][name] = participationMap.get(reply, "TENTATIVE")

    return state


def extract(input):
    return reduce(
        transformer,
        re.findall(r"vote (\w+)\" title=\"(.+?): (.+?)\"", input, re.DOTALL),
        {},
    )


r = requests.get("https://dud-poll.inf.tu-dresden.de/laufschule-kempten/")
availability = extract(r.text)

cal = Calendar()
cal.add("version", "2.0")
cal.add("prodid", "-//eis-kempten//esc-kempten.de//team-laufschule")

cancelled_times = [pd.Timestamp("2023-12-28T15:45"), pd.Timestamp("2024-01-04T15:45")]

for time in (
    pd.date_range(
        start="2023-09-23T09:00", end="2024-03-30T09:00", freq="W-SAT"
    ).tolist()
    + pd.date_range(
        start="2023-09-28T15:45", end="2024-03-30T15:45", freq="W-THU"
    ).tolist()
):
    description = []

    event = Event()
    event.add("summary", "🦈 Team Laufschule")
    event.add("status", "CANCELLED" if time in cancelled_times else "CONFIRMED")
    event.add("dtstart", time)
    event.add("dtend", time + timedelta(hours=1))
    event.add("dtstamp", datetime.now())
    event.add(
        "location", "Eisstadion Kempten, Memminger Str. 137, 87439 Kempten (Allgäu)"
    )
    event.add("geo", vGeo((47.7445565, 10.3025167)))

    for name, status in sorted(availability.get(time.isoformat(), {}).items()):
        description.append(iconMap[status] + " " + name)
        attendee = vText("")
        attendee.params["cn"] = vText(name)
        attendee.params["PARTSTAT"] = vText(status)
        event.add("attendee", attendee, encode=0)

    description.append("\nZuletzt aktualisiert: " + datetime.now().isoformat())
    event.add("description", "\n".join(description))
    cal.add_component(event)

os.makedirs("build/esc-kempten/", exist_ok=True)
with open("build/esc-kempten/team-laufschule.ics", "wb") as file:
    file.write(cal.to_ical())
