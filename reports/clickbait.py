from models.video_metrics import VideoMetric
from .base import Report
from reports.registry import register_report


@register_report("clickbait")
class Clickbait(Report[VideoMetric]):
    def generate(self, rows: list[VideoMetric]) -> list[VideoMetric]:

        data: list[VideoMetric] = [
            VideoMetric(row.title, row.ctr, row.retention_rate)
            for row in rows
            if row.ctr > 15 and row.retention_rate < 40
        ]

        return sorted(data, key=lambda x: x.ctr, reverse=True)
