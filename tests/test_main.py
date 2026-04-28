import pytest

from main import get_report
from services.csv_reader import read_csv
from services.parser import parse_metrics_row
from models.video_metrics import VideoMetric


@pytest.fixture
def sample_file(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Я бросил IT и стал фермером,18.2,35,45200,1240,4.2\n"
        "Как я спал по 4 часа и ничего не понял,22.5,48,128700,3150,3.1\n"
        "Почему сеньоры не носят галстуки,9.5,82,31500,890,8.9\n"
    )

    return csv_file


def test_csv_integration(sample_file):
    rows = read_csv(sample_file)
    records = [parse_metrics_row(row) for row in rows]
    report = get_report("clickbait")
    result = report.generate(records)

    expected_row = [
        VideoMetric(title="Я бросил IT и стал фермером", ctr=18.2, retention_rate=35)
    ]
    assert result == expected_row


def test_main_cli(monkeypatch, sample_file, capsys):
    import main

    monkeypatch.setattr(
        "sys.argv", ["main.py", "-f", str(sample_file), "-r", "clickbait"]
    )
    main.main()
    captured = capsys.readouterr()
    print(captured)
    assert "Я бросил IT и стал фермером" in captured.out
    assert "18.2" in captured.out
    assert "35" in captured.out
