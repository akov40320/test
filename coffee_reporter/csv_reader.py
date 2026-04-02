from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from .models import StudentActivity

REQUIRED_COLUMNS = {"student", "coffee_spent"}


def read_activities(file_paths: Iterable[Path]) -> list[StudentActivity]:
    activities: list[StudentActivity] = []

    for file_path in file_paths:
        if not file_path.exists() or not file_path.is_file():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = set(reader.fieldnames or [])
            missing_columns = REQUIRED_COLUMNS - fieldnames
            if missing_columns:
                missing = ", ".join(sorted(missing_columns))
                raise ValueError(
                    f"В файле {file_path} отсутствуют обязательные колонки: {missing}"
                )

            for row in reader:
                activities.append(
                    StudentActivity(
                        student=row["student"],
                        coffee_spent=float(row["coffee_spent"]),
                    )
                )

    return activities
