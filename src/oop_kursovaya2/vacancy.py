from typing import Optional, Dict, Any


class Vacancy:
    """Класс предназначен для представления и сравнения вакансий"""

    __slots__ = ('name', 'city', 'url', 'salary_from', 'salary_to', 'currency')

    def __init__(self, name, city, url, salary_from: Optional[int], salary_to: Optional[int], currency: Optional[str]):
        self.name = self._validate_string(name)
        self.city = self._validate_string(city)
        self.url = self._validate_string(url)
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.currency = self._validate_string(currency)

    def _validate_string(self, value: Optional[str]) -> str:
        """Проверяет, что значение является строкой"""
        return str(value) if value is not None else ""

    def _validate_salary(self, value: Optional[int]) -> int:
        """Проверяет, что значение является положительным числом или None"""
        return int(value) if value is not None and value >= 0 else 0

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        return self. salary_from == other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def to_dict(self) -> Dict[str, Any]:
        """Возвращает вакансию в виде словаря."""
        return {
            'name': self.name,
            'city': self.city,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency
        }

    def __gt__(self, other): return self.salary_from > other.salary_from
    def __lt__(self, other): return self.salary_from < other.salary_from
    def __eq__(self, other): return self.salary_from == other.salary_from
