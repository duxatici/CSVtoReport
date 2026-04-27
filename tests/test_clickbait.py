import pytest

from models.video_metrics import VideoMetric
from reports.clickbait import Clickbait, ClickbaitRow


@pytest.mark.parametrize(
    "records, expected",
    [
        # записи подходящие и не подходящие под фильтр
        (
            [
                VideoMetric("Я бросил IT и стал фермером", 18.2, 35),
                VideoMetric("Как я спал по 4 часа и ничего не понял", 22.5, 48),
                VideoMetric("Почему сеньоры не носят галстуки", 9.5, 82),
            ],
            [
                ClickbaitRow(
                    title="Я бросил IT и стал фермером", ctr=18.2, retention_rate=35
                )
            ],
        ),
        # ни одна запись не подходит под фильтр
        ([VideoMetric("Почему сеньоры не носят галстуки", 9.5, 82)], []),
        # сортировка
        (
            [
                VideoMetric("Я бросил IT и стал фермером", 18.2, 35),
                VideoMetric("Как я спал по 4 часа и ничего не понял", 22.5, 38),
                VideoMetric("Почему сеньоры не носят галстуки", 9.5, 82),
            ],
            [
                ClickbaitRow(
                    title="Как я спал по 4 часа и ничего не понял",
                    ctr=22.5,
                    retention_rate=38,
                ),
                ClickbaitRow(
                    title="Я бросил IT и стал фермером", ctr=18.2, retention_rate=35
                ),
            ],
        ),
    ],
)
def test_report(records, expected):
    report = Clickbait()
    result = report.generate(records)
    assert result == expected
