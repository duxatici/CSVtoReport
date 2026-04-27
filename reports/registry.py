import logging

from exceptions import ReportNotFoundError

from .base import Report

logger = logging.getLogger(__name__)

REPORTS: dict[str, type[Report]] = {}


def register_report(name: str):
    def decorator(cls):
        if not issubclass(cls, Report):
            raise TypeError(f"Отчет {cls} не является наследуемым от класса Report")
        if name in REPORTS:
            raise ValueError(f"Отчет с именем {name} уже зарегистрирован")

        REPORTS[name] = cls
        logger.info(f"Отчет {name} зарегистрирован")

        return cls

    return decorator


def get_report(name: str) -> Report:
    try:
        return REPORTS[name]()
    except KeyError:
        raise ReportNotFoundError(f"Неизвестный отчет: {name}")
