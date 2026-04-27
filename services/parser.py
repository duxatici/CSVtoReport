from exceptions import InvalidRowError
from models.video_metrics import VideoMetric


def parse_metrics_row(row: dict[str, str]) -> VideoMetric:
    try:
        return VideoMetric(
            title=row["title"],
            ctr=float(row["ctr"]),
            retention_rate=int(row["retention_rate"]),
        )
    except KeyError as e:
        raise InvalidRowError(f"Отсутствует ключ в строке: {e}") from e
    except ValueError as e:
        raise InvalidRowError(f"Неверное значение в строке: {row}") from e
