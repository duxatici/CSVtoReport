from abc import ABC, abstractmethod

from models.video_metrics import VideoMetric


class Report[T](ABC):
    @abstractmethod
    def generate(self, rows: list[VideoMetric]) -> list[T]:
        pass
