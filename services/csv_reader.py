import csv
import logging

from exceptions import FileReadError

logger = logging.getLogger(__name__)


def read_csv(file_path: str) -> list[dict[str, str]]:
    try:
        with open(file_path, encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            return [
                {key: value.strip() for key, value in row.items()} for row in reader
            ]
    except FileNotFoundError as e:
        raise FileReadError(f"Файл не найден: {file_path}") from e
    except OSError as e:
        raise FileReadError(f"Ошибка чтения файла: {file_path}") from e


def read_csv_many(paths: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for file_path in paths:
        rows.extend(read_csv(file_path))

    return rows
