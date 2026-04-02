from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from .csv_reader import read_activities
from .registry import get_report
from .render import render_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Формирование отчетов по CSV-файлам подготовки студентов к экзаменам."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        metavar="CSV",
        help="Пути к CSV-файлам с данными студентов.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчета (поддерживается: median-coffee).",
    )
    return parser


def run(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    file_paths = [Path(file_name) for file_name in args.files]

    try:
        report = get_report(args.report)
        activities = read_activities(file_paths)
    except (FileNotFoundError, ValueError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 2

    rows = report.build(activities)
    print(render_table(report.headers, rows))
    return 0
