from icalendar import Event, vGeo
from datetime import datetime


def compute_event(start, end, summary):
    event = Event()
    event.add("summary", summary)
    event.add("dtstart", start)
    event.add("dtend", end)
    event.add("dtstamp", datetime.now())
    event.add(
        "location", "Eisstadion Kempten, Memminger Str. 137, 87439 Kempten (Allgäu)"
    )
    event.add("geo", vGeo((47.7445565, 10.3025167)))
    event.add("url", "https://www.eisstadion-kempten.de/")

    return event
