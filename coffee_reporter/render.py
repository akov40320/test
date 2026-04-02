from __future__ import annotations

from typing import Sequence

from .reports.base import ReportRow

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None


def _format_value(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}"


def _manual_table(headers: Sequence[str], rows: Sequence[ReportRow]) -> str:
    raw_rows = [(row.student, _format_value(row.value)) for row in rows]
    widths = [len(str(headers[0])), len(str(headers[1]))]
    for student, value in raw_rows:
        widths[0] = max(widths[0], len(student))
        widths[1] = max(widths[1], len(value))

    separator = f"+-{'-' * widths[0]}-+-{'-' * widths[1]}-+"
    lines = [
        separator,
        f"| {headers[0].ljust(widths[0])} | {headers[1].ljust(widths[1])} |",
        separator,
    ]
    for student, value in raw_rows:
        lines.append(f"| {student.ljust(widths[0])} | {value.rjust(widths[1])} |")
    lines.append(separator)
    return "\n".join(lines)


def render_table(headers: Sequence[str], rows: Sequence[ReportRow]) -> str:
    table_rows = [(row.student, _format_value(row.value)) for row in rows]
    if tabulate is None:
        return _manual_table(headers, rows)
    return tabulate(table_rows, headers=headers, tablefmt="github")
