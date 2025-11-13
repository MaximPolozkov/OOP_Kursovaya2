from oop_kursovaya2.vacancy import Vacancy


def test_vacancy_initialization(vacancy):
    """Тест проверяет, корректно ли инициализируются поля объекта."""
    assert vacancy.name == "Python Developer"
    assert vacancy.city == "Moscow"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary_from == 1000
    assert vacancy.salary_to == 1500
    assert vacancy.currency == "RUB"


def test_vacancy_comparisons(vacancy):
    """Тест проверяет работу операторов сравнения между объектами Vacancy."""
    vacancy2 = Vacancy("Java Developer", "St. Petersburg", "http://example.com", 1200, 1800, "RUB")

    assert vacancy < vacancy2
    assert vacancy2 > vacancy
    assert vacancy != vacancy2
    vacancy3 = Vacancy("Data Scientist", "Moscow", "http://example.com", 1000, 1300, "RUB")
    assert vacancy == vacancy3
