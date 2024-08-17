from icalendar import Calendar, Event, vGeo
from datetime import datetime, timedelta
import pandas as pd
import dateparser
import functools
import itertools
import requests
import os
import re


def transform(entry, ref_date):
    date = re.search(r">\w+,(\s+\d+[\.,]\s*\w+)\s+", entry)

    if not date:
        return None

    dt = dateparser.parse(date.groups(1)[0], settings={"TIMEZONE": "Europe/Berlin"})

    if not dt:
        return None

    # handle entries from the next year
    # presumably those where the month is lower than what we currently have
    if dt.month < ref_date.month:
        dt = dt.replace(year=ref_date.year + 1)
    else:
        dt = dt.replace(year=ref_date.year)

    disco = re.search(r"Disco", entry, re.IGNORECASE)

    times = re.findall(r"(\d\d):(\d\d)\s+&#8211;\s+(\d\d):(\d\d)\s+Uhr", entry)

    return [
        (
            dt.replace(hour=int(time[0]), minute=int(time[1])),
            dt.replace(hour=int(time[2]), minute=int(time[3])),
            "⛸️ Öffentlicher Lauf" if disco is None else "🪩 ICE-Disco",
        )
        for time in times
    ]


def extract(input, ref_date):
    match = re.search(
        r">Öffentlicher Lauf</[^>]+>\s+<div[^>]+>(.+?)</div>", input, re.DOTALL
    )

    if not match:
        return []

    dates = match.groups(1)[0].splitlines()
    return list(
        itertools.chain.from_iterable(
            filter(None, map(functools.partial(transform, ref_date=ref_date), dates))
        )
    )


updated_at = "Zuletzt aktualisiert: " + datetime.now().isoformat()


def compute_event(start, end, description):
    event = Event()
    event.add("summary", description)
    event.add("dtstart", start)
    event.add("dtend", end)
    event.add("dtstamp", datetime.now())
    event.add(
        "location", "Eisstadion Kempten, Memminger Str. 137, 87439 Kempten (Allgäu)"
    )
    event.add("geo", vGeo((47.7445565, 10.3025167)))
    event.add("description", updated_at)
    event.add("url", "https://www.eisstadion-kempten.de/")

    return event


if __name__ == "__main__":
    cal = Calendar()
    cal.add("version", "2.0")
    cal.add("prodid", "-//eis-kempten//eisstadion-kempten.de//oeffentlicher-lauf")

    r = requests.get("https://www.eisstadion-kempten.de")
    for start, end, description in extract(r.text, datetime.now()):
        cal.add_component(compute_event(start, end, description))

    for start in (
        pd.date_range(
            start="2024-09-24T13:45", end="2025-03-25T13:45", freq="W-TUE"
        ).tolist()
        + pd.date_range(
            start="2024-09-25T13:45", end="2025-03-26T13:45", freq="W-WED"
        ).tolist()
        + pd.date_range(
            start="2024-09-27T14:00", end="2025-03-28T14:00", freq="W-FRI"
        ).tolist()
        + pd.date_range(
            start="2024-09-28T14:00", end="2025-03-29T14:00", freq="W-SAT"
        ).tolist()
        + pd.date_range(
            start="2024-09-29T09:45", end="2025-03-30T09:45", freq="W-SUN"
        ).tolist()
        + pd.date_range(
            start="2024-09-29T14:00", end="2025-03-30T14:00", freq="W-SUN"
        ).tolist()
    ):
        cal.add_component(
            compute_event(start, start + timedelta(minutes=105), "⛸️ Öffentlicher Lauf")
        )
    for start in pd.date_range(
        start="2024-09-28T19:45", end="2025-03-29T19:45", freq="W-SAT"
    ).tolist():
        cal.add_component(
            compute_event(start, start + timedelta(minutes=105), "🪩 ICE-Disco")
        )

    os.makedirs("build/eisstadion-kempten/", exist_ok=True)
    with open("build/eisstadion-kempten/oeffentlicher-lauf.ics", "wb") as file:
        file.write(cal.to_ical())
