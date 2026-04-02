from coffee_reporter.models import StudentActivity
from coffee_reporter.reports.median_coffee import MedianCoffeeReport


def test_median_report_builds_and_sorts_descending() -> None:
    activities = [
        StudentActivity(student="Ann", coffee_spent=100),
        StudentActivity(student="Ann", coffee_spent=250),
        StudentActivity(student="Ben", coffee_spent=300),
        StudentActivity(student="Ben", coffee_spent=500),
        StudentActivity(student="Cara", coffee_spent=200),
    ]

    rows = MedianCoffeeReport().build(activities)

    assert [(row.student, row.value) for row in rows] == [
        ("Ben", 400.0),
        ("Cara", 200.0),
        ("Ann", 175.0),
    ]

    assert rows[0].value >= rows[1].value >= rows[2].value
