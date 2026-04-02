from pathlib import Path

import pytest

from coffee_reporter.csv_reader import read_activities


def test_read_activities_from_multiple_files(tmp_path: Path) -> None:
    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"

    first.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ann,2024-06-01,100,7,3,ok,Math\n",
        encoding="utf-8",
    )
    second.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ben,2024-06-01,200,6,4,ok,Physics\n",
        encoding="utf-8",
    )

    activities = read_activities([first, second])

    assert len(activities) == 2
    assert activities[0].student == "Ann"
    assert activities[1].student == "Ben"


def test_read_activities_raises_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_activities([missing])
