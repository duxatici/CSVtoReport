from pathlib import Path

import pytest

from exceptions import FileReadError
from services.csv_reader import read_csv


def test_file_not_found():
    non_existent_file = Path("non_existent.csv")
    with pytest.raises(FileReadError):
        read_csv(non_existent_file)
