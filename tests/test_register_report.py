import pytest

from exceptions import ReportNotFoundError
from main import get_report
from reports.base import Report
from reports.clickbait import Clickbait
from reports.registry import register_report


@pytest.fixture
def temp_reports(monkeypatch):
    temp = {}
    monkeypatch.setattr("reports.registry.REPORTS", temp)
    return temp


def test_register_report():
    from reports.registry import REPORTS

    assert "clickbait" in REPORTS.keys()


def test_get_report():
    report = get_report("clickbait")
    assert isinstance(report, Clickbait)


def test_unknown_report():
    with pytest.raises(ReportNotFoundError):
        get_report("unknown")


def test_duplicate_report_name(temp_reports):
    class DummyReport(Report):
        pass

    register_report("duplicate_name")(DummyReport)
    assert temp_reports.get("duplicate_name") is DummyReport
    with pytest.raises(
        ValueError, match="Отчет с именем duplicate_name уже зарегистрирован"
    ):
        register_report("duplicate_name")(DummyReport)


def test_not_class_report():
    with pytest.raises(TypeError) as e:
        register_report("not_class")(int)
    assert "не является наследуемым от класса Report" in str(e.value)
