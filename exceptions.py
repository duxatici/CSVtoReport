class AppError(Exception):
    pass


class FileReadError(AppError):
    pass


class InvalidRowError(AppError):
    pass


class ReportNotFoundError(AppError):
    pass
