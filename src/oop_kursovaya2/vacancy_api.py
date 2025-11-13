from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Абстрактный метод для работы с вакансиями API"""
    @abstractmethod
    def get_vacancies(self):
        pass
