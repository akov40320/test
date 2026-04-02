from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence

from ..models import StudentActivity


@dataclass(frozen=True, slots=True)
class ReportRow:
    student: str
    value: float


class Report(Protocol):
    slug: str
    title: str
    headers: Sequence[str]

    def build(self, activities: Sequence[StudentActivity]) -> list[ReportRow]:
        ...
