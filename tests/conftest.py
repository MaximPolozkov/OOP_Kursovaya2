import pytest

from oop_kursovaya2.json_server import JSONSaver
from oop_kursovaya2.vacancy import Vacancy


@pytest.fixture
def vacancy():
    """Фикстура для создания объекта Vacancy"""
    return Vacancy("Python Developer", "Moscow", "http://example.com", 1000, 1500, "RUB")


@pytest.fixture
def json_saver(tmpdir):
    """Фикстура для json_saver, используем временный файл для тестов"""
    filename = tmpdir.join("vacancies.json")
    return JSONSaver(filename=str(filename))
