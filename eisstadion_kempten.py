from icalendar import Calendar, Event, vGeo
from datetime import datetime
import dateparser
import itertools
import requests
import os
import re

def transform(entry):
    date = re.search(
        r">(\w+,\s+\d+[\.,]\s*\w+)\s+",
        entry
    )

    if not date:
        return None

    dt = dateparser.parse(date.groups(1)[0], settings={'TIMEZONE': 'Europe/Berlin'})

    disco = re.search(
        r"Disco",
        entry,
        re.IGNORECASE
    )

    times = re.findall(
        r"(\d\d):(\d\d)\s+&#8211;\s+(\d\d):(\d\d)\s+Uhr",
        entry
    )

    return [(
        dt.replace(hour=int(time[0]), minute=int(time[1])),
        dt.replace(hour=int(time[2]), minute=int(time[3])),
        "⛸️ Öffentlicher Lauf" if disco is None else "🪩 ICE-Disco"
    ) for time in times]

def extract(input):
    match = re.search(
        r">Öffentlicher Lauf</[^>]+>\s+<div[^>]+>(.+?)</div>",
        input,
        re.DOTALL
    )
    dates = match.groups(1)[0].splitlines()
    return list(itertools.chain.from_iterable(filter(None, map(transform, dates))))

if __name__ == "__main__":
    cal = Calendar()
    cal.add('version', '2.0')
    cal.add('prodid', '-//eis-kempten//eisstadion-kempten.de//oeffentlicher-lauf')

    r = requests.get("https://www.eisstadion-kempten.de")
    for (start, end, description) in extract(r.text):
        event = Event()
        event.add('summary', description)
        event.add('dtstart', start)
        event.add('dtend', end)
        event.add('dtstamp', datetime.now())
        event.add('location', 'Eisstadion Kempten, Memminger Str. 137, 87439 Kempten (Allgäu)')
        event.add('geo', vGeo((47.7445565, 10.3025167)))
        cal.add_component(event)

    os.makedirs('build/eisstadion-kempten/', exist_ok=True)
    with open('build/eisstadion-kempten/oeffentlicher-lauf.ics', 'wb') as file:
        file.write(cal.to_ical())
