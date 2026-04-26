from dataclasses import dataclass


@dataclass
class VideoMetric:
    title: str
    ctr: float
    retention_rate: int
