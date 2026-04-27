import pytest

from exceptions import InvalidRowError
from models.video_metrics import VideoMetric
from services.parser import parse_metrics_row


@pytest.mark.parametrize(
    "row, expected_title, expected_ctr, expected_retention_rate",
    [
        (
            {
                "title": "Я бросил IT и стал фермером",
                "ctr": "18.2",
                "retention_rate": "35",
                "views": "45200",
                "likes": "1240",
                "avg_watch_time": "4.2",
            },
            "Я бросил IT и стал фермером",
            18.2,
            35,
        ),
        (
            {
                "title": "Как я спал по 4 часа и ничего не понял",
                "ctr": "22.5",
                "retention_rate": "28",
                "views": "128700",
                "likes": "3150",
                "avg_watch_time": "3.1",
            },
            "Как я спал по 4 часа и ничего не понял",
            22.5,
            28,
        ),
    ],
)
def test_parse_student_row_valid(
    row, expected_title, expected_ctr, expected_retention_rate
):
    record = parse_metrics_row(row)
    assert isinstance(record, VideoMetric)
    assert record.title == expected_title
    assert record.ctr == expected_ctr
    assert record.retention_rate == expected_retention_rate


@pytest.mark.parametrize(
    "row",
    [
        {
            "ctr": "18.2",
            "retention_rate": "35",
            "views": "45200",
            "likes": "1240",
            "avg_watch_time": "4.2",
        },
        {
            "title": "Я бросил IT и стал фермером",
            "retention_rate": "35",
            "views": "45200",
            "likes": "1240",
            "avg_watch_time": "4.2",
        },
        {
            "title": "Я бросил IT и стал фермером",
            "ctr": "18.2",
            "views": "45200",
            "likes": "1240",
            "avg_watch_time": "4.2",
        },
    ],
)
def test_parse_student_row_missing_key(row):
    with pytest.raises(InvalidRowError) as e:
        parse_metrics_row(row)
    assert "Отсутствует ключ" in str(e.value)


@pytest.mark.parametrize(
    "row",
    [
        {
            "title": "Я бросил IT и стал фермером",
            "ctr": "word",
            "retention_rate": "35",
            "views": "45200",
            "likes": "1240",
            "avg_watch_time": "4.2",
        },
        {
            "title": "Я бросил IT и стал фермером",
            "ctr": "18.2",
            "retention_rate": "3.5",
            "views": "45200",
            "likes": "1240",
            "avg_watch_time": "4.2",
        },
    ],
)
def test_parse_student_row_invalid_value(row):
    with pytest.raises(InvalidRowError) as e:
        parse_metrics_row(row)
    assert "Неверное значение" in str(e.value)
