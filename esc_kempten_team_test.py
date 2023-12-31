from esc_kempten_team import extract
from datetime import datetime


def test_01():
    with open("./tests/laufschule-kempten/01.html") as file:
        content = file.read()

    assert extract(content) == {
        "2023-09-23T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "DECLINED",
            "Michi": "DECLINED",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2023-09-28T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-09-30T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-05T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-07T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-12T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-10-14T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-10-19T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-21T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-26T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-28T09:00:00": {
            "Ailine": "DECLINED",
            "Celine": "DECLINED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-02T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-04T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-09T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-11T09:00:00": {
            "Ailine": "DECLINED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-16T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-18T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-11-23T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-25T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "DECLINED",
        },
        "2023-11-30T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-02T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "DECLINED",
        },
        "2023-12-07T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-09T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-14T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-16T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-21T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-23T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2023-12-28T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-12-30T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
    }


def test_02():
    with open("./tests/laufschule-kempten/02.html") as file:
        content = file.read()

    assert extract(content) == {
        "2023-09-23T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "DECLINED",
            "Michi": "DECLINED",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2023-09-28T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-09-30T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-05T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-07T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-12T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-10-14T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-10-19T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-21T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-26T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-10-28T09:00:00": {
            "Ailine": "DECLINED",
            "Celine": "DECLINED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-02T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-04T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "ACCEPTED",
            "Henne": "DECLINED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-09T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-11T09:00:00": {
            "Ailine": "DECLINED",
            "Celine": "ACCEPTED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-16T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-18T09:00:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-11-23T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-11-25T09:00:00": {
            "Ailine": "DECLINED",
            "Celine": "DECLINED",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "ACCEPTED",
            "Stefan": "DECLINED",
        },
        "2023-11-30T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-02T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "DECLINED",
        },
        "2023-12-07T15:45:00": {
            "Ailine": "ACCEPTED",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-09T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "DECLINED",
        },
        "2023-12-14T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "DECLINED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-16T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "ACCEPTED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-21T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "ACCEPTED",
        },
        "2023-12-23T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2023-12-28T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2023-12-30T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "ACCEPTED",
            "Michi": "ACCEPTED",
            "Nadja": "DECLINED",
            "Stefan": "DECLINED",
        },
        "2024-01-04T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-01-06T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-01-11T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-01-13T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "DECLINED",
        },
        "2024-01-18T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-01-20T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-01-25T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-01-27T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-02-01T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-02-03T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-02-08T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-02-10T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-02-15T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-02-17T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-02-22T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
        "2024-02-24T09:00:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "TENTATIVE",
        },
        "2024-02-29T15:45:00": {
            "Ailine": "TENTATIVE",
            "Celine": "TENTATIVE",
            "Henne": "TENTATIVE",
            "Michi": "TENTATIVE",
            "Nadja": "TENTATIVE",
            "Stefan": "ACCEPTED",
        },
    }
