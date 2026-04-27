# ruff: noqa: F401
import logging

from tabulate import tabulate

from logger import init_logger
from exceptions import AppError
from services.csv_reader import read_csv_many
from services.parser import parse_metrics_row
from reports.clickbait import Clickbait
from models.video_metrics import VideoMetric

logger = logging.getLogger(__name__)


def main():
    try:
        rows = read_csv_many(["file_examples/stats1.csv", "file_examples/stats2.csv"])

        records = [parse_metrics_row(row) for row in rows]

        report = Clickbait()

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
