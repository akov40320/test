from pathlib import Path

from coffee_reporter.cli import run


def test_cli_returns_error_for_unknown_report(capsys) -> None:
    exit_code = run(["--files", "math.csv", "--report", "unknown-report"])
    captured = capsys.readouterr()

    assert exit_code == 2
    assert "Неизвестный отчет" in captured.err


def test_cli_prints_median_coffee_table(tmp_path: Path, capsys) -> None:
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ann,2024-06-01,100,7,3,ok,Math\n"
        "Ann,2024-06-02,200,6,4,tired,Math\n"
        "Ben,2024-06-01,250,6,5,ok,Math\n",
        encoding="utf-8",
    )

    exit_code = run(["--files", str(csv_file), "--report", "median-coffee"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Студент" in captured.out
    assert "Медиана трат на кофе" in captured.out
    assert "Ben" in captured.out
    assert "Ann" in captured.out
