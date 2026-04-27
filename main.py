# ruff: noqa: F401
import logging
import argparse

from tabulate import tabulate

from exceptions import AppError
from reports.registry import REPORTS, get_report
from services.csv_reader import read_csv_many
from services.parser import parse_metrics_row
from reports.clickbait import Clickbait

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Генерирует отчет из CSV файла")
    parser.add_argument(
        "-f",
        "--files",
        type=str,
        nargs="+",
        required=True,
        help="CSV файлы для обработки",
    )
    parser.add_argument(
        "-r",
        "--report",
        type=str,
        choices=REPORTS.keys(),
        default="clickbait",
        help="Тип отчета для генерации",
    )

    return parser.parse_args()


def main():
    try:
        args = parse_args()

        rows = read_csv_many(args.files)

        records = [parse_metrics_row(row) for row in rows]

        report = get_report(args.report)

        generated_report = report.generate(records)

        table = tabulate(
            generated_report,
            headers=["Title", "Ctr", "Retention rate"],
            tablefmt="fancy_grid",
        )

        print(table)

    except AppError as e:
        logger.error(f"Ошибка: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
