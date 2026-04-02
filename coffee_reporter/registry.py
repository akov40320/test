from __future__ import annotations

from typing import Mapping

from .reports import MedianCoffeeReport, Report

REPORTS: Mapping[str, Report] = {
    MedianCoffeeReport.slug: MedianCoffeeReport(),
}


def get_report(report_name: str) -> Report:
    try:
        return REPORTS[report_name]
    except KeyError as error:
        available = ", ".join(sorted(REPORTS))
        raise ValueError(
            f"Неизвестный отчет '{report_name}'. Доступные отчеты: {available}"
        ) from error
