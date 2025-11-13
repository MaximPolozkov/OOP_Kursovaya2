class Vacancy:
    """Класс предназначен для представления и сравнения вакансий"""
    def __init__(self, name, city, url, salary_from, salary_to, currency):
        self.name = name
        self.city = city
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.currency = currency

    def __gt__(self, other): return self.salary_from > other.salary_from
    def __lt__(self, other): return self.salary_from < other.salary_from
    def __eq__(self, other): return self.salary_from == other.salary_from
