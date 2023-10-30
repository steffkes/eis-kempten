from eisstadion_kempten import extract
from datetime import datetime


def test_01():
    with open("./tests/01.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 9, 26, 13, 45),
            datetime(2023, 9, 26, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 27, 13, 45),
            datetime(2023, 9, 27, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 29, 14, 0),
            datetime(2023, 9, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 30, 14, 0),
            datetime(2023, 9, 30, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 9, 30, 19, 45), datetime(2023, 9, 30, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 1, 9, 45),
            datetime(2023, 10, 1, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 14, 0),
            datetime(2023, 10, 1, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 3, 13, 45),
            datetime(2023, 10, 3, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 4, 13, 45),
            datetime(2023, 10, 4, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 6, 14, 0),
            datetime(2023, 10, 6, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 7, 14, 0),
            datetime(2023, 10, 7, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
    ]


def test_02():
    with open("./tests/02.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 9, 29, 14, 0),
            datetime(2023, 9, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 30, 14, 0),
            datetime(2023, 9, 30, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 9, 30, 19, 45), datetime(2023, 9, 30, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 1, 9, 45),
            datetime(2023, 10, 1, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 14, 0),
            datetime(2023, 10, 1, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 3, 13, 45),
            datetime(2023, 10, 3, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 4, 13, 45),
            datetime(2023, 10, 4, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 6, 14, 0),
            datetime(2023, 10, 6, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 7, 14, 0),
            datetime(2023, 10, 7, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
    ]


def test_03():
    with open("./tests/03.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 9, 29, 14, 0),
            datetime(2023, 9, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 30, 14, 0),
            datetime(2023, 9, 30, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 30, 19, 45),
            datetime(2023, 9, 30, 21, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 9, 45),
            datetime(2023, 10, 1, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 14, 0),
            datetime(2023, 10, 1, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 3, 13, 45),
            datetime(2023, 10, 3, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 4, 13, 45),
            datetime(2023, 10, 4, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 6, 14, 0),
            datetime(2023, 10, 6, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 7, 14, 0),
            datetime(2023, 10, 7, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 7, 19, 0), datetime(2023, 10, 7, 20, 45), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 8, 9, 45),
            datetime(2023, 10, 8, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 8, 14, 0),
            datetime(2023, 10, 8, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 10, 13, 45),
            datetime(2023, 10, 10, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 11, 13, 45),
            datetime(2023, 10, 11, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 13, 14, 0),
            datetime(2023, 10, 13, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 14, 14, 0),
            datetime(2023, 10, 14, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 14, 19, 45), datetime(2023, 10, 14, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 15, 9, 45),
            datetime(2023, 10, 15, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
    ]


def test_04():
    with open("./tests/04.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 9, 29, 14, 0),
            datetime(2023, 9, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 9, 30, 14, 0),
            datetime(2023, 9, 30, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 9, 45),
            datetime(2023, 10, 1, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 1, 14, 0),
            datetime(2023, 10, 1, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 3, 13, 45),
            datetime(2023, 10, 3, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 4, 13, 45),
            datetime(2023, 10, 4, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 6, 14, 0),
            datetime(2023, 10, 6, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 7, 14, 0),
            datetime(2023, 10, 7, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 7, 19, 45), datetime(2023, 10, 7, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 8, 9, 45),
            datetime(2023, 10, 8, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 8, 14, 0),
            datetime(2023, 10, 8, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 10, 13, 45),
            datetime(2023, 10, 10, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 11, 13, 45),
            datetime(2023, 10, 11, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 13, 14, 0),
            datetime(2023, 10, 13, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 14, 14, 0),
            datetime(2023, 10, 14, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 14, 19, 45), datetime(2023, 10, 14, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 15, 9, 45),
            datetime(2023, 10, 15, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 15, 14, 0),
            datetime(2023, 10, 15, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 17, 13, 45),
            datetime(2023, 10, 17, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 18, 13, 45),
            datetime(2023, 10, 18, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 20, 14, 0),
            datetime(2023, 10, 20, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 21, 14, 0),
            datetime(2023, 10, 21, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 21, 19, 0),
            datetime(2023, 10, 21, 20, 45),
            "⛸️ Öffentlicher Lauf",
        ),
    ]


def test_05():
    with open("./tests/05.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 10, 4, 13, 45),
            datetime(2023, 10, 4, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 6, 14, 0),
            datetime(2023, 10, 6, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 7, 14, 0),
            datetime(2023, 10, 7, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 7, 19, 45), datetime(2023, 10, 7, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 8, 9, 45),
            datetime(2023, 10, 8, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 8, 14, 0),
            datetime(2023, 10, 8, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 10, 13, 45),
            datetime(2023, 10, 10, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 11, 13, 45),
            datetime(2023, 10, 11, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 13, 14, 0),
            datetime(2023, 10, 13, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 14, 14, 0),
            datetime(2023, 10, 14, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 14, 19, 45), datetime(2023, 10, 14, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 15, 9, 45),
            datetime(2023, 10, 15, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 15, 14, 0),
            datetime(2023, 10, 15, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 17, 13, 45),
            datetime(2023, 10, 17, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 18, 13, 45),
            datetime(2023, 10, 18, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 20, 14, 0),
            datetime(2023, 10, 20, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 21, 14, 0),
            datetime(2023, 10, 21, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 21, 19, 0), datetime(2023, 10, 21, 20, 45), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 24, 13, 45),
            datetime(2023, 10, 24, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 25, 13, 45),
            datetime(2023, 10, 25, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 27, 14, 0),
            datetime(2023, 10, 27, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 28, 14, 0),
            datetime(2023, 10, 28, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 28, 19, 45), datetime(2023, 10, 28, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 29, 9, 45),
            datetime(2023, 10, 29, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 29, 14, 0),
            datetime(2023, 10, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 31, 13, 45),
            datetime(2023, 10, 31, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
    ]


def test_06():
    with open("./tests/06.html") as file:
        content = file.read()

    assert extract(content) == [
        (
            datetime(2023, 10, 21, 14, 0),
            datetime(2023, 10, 21, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 21, 19, 0), datetime(2023, 10, 21, 20, 45), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 24, 13, 45),
            datetime(2023, 10, 24, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 25, 13, 45),
            datetime(2023, 10, 25, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 27, 14, 0),
            datetime(2023, 10, 27, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 28, 14, 0),
            datetime(2023, 10, 28, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 10, 28, 19, 45), datetime(2023, 10, 28, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 10, 29, 9, 45),
            datetime(2023, 10, 29, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 29, 14, 0),
            datetime(2023, 10, 29, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 10, 31, 13, 45),
            datetime(2023, 10, 31, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 1, 13, 45),
            datetime(2023, 11, 1, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 3, 14, 0),
            datetime(2023, 11, 3, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 4, 14, 0),
            datetime(2023, 11, 4, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (datetime(2023, 11, 4, 19, 45), datetime(2023, 11, 4, 21, 30), "🪩 ICE-Disco"),
        (
            datetime(2023, 11, 5, 9, 45),
            datetime(2023, 11, 5, 11, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 5, 14, 0),
            datetime(2023, 11, 5, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 7, 13, 45),
            datetime(2023, 11, 7, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 8, 13, 45),
            datetime(2023, 11, 8, 15, 30),
            "⛸️ Öffentlicher Lauf",
        ),
        (
            datetime(2023, 11, 11, 14, 0),
            datetime(2023, 11, 11, 15, 45),
            "⛸️ Öffentlicher Lauf",
        ),
    ]
