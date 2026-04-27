from typing import NamedTuple

from models.video_metrics import VideoMetric
from .base import Report
from reports.registry import register_report


class ClickbaitRow(NamedTuple):
    title: str
    ctr: float
    retention_rate: float


@register_report("clickbait")
class Clickbait(Report[ClickbaitRow]):
    def generate(self, rows: list[VideoMetric]) -> list[ClickbaitRow]:

        data: list[ClickbaitRow] = [
            ClickbaitRow(row.title, row.ctr, row.retention_rate)
            for row in rows
            if row.ctr > 15 and row.retention_rate < 40
        ]

        return sorted(data, key=lambda x: x.ctr, reverse=True)
