from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Sequence

from ..models import StudentActivity
from .base import ReportRow


class MedianCoffeeReport:
    slug = "median-coffee"
    title = "Медианные траты на кофе по студентам"
    headers = ("Студент", "Медиана трат на кофе")

    def build(self, activities: Sequence[StudentActivity]) -> list[ReportRow]:
        grouped: dict[str, list[float]] = defaultdict(list)
        for activity in activities:
            grouped[activity.student].append(activity.coffee_spent)

        rows = [ReportRow(student=student, value=median(values)) for student, values in grouped.items()]
        return sorted(rows, key=lambda row: (-row.value, row.student))
