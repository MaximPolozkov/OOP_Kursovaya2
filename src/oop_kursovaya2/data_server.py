from abc import ABC, abstractmethod


class DataServer(ABC):
    """Абстрактный метод для записи данных в бд"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в бд"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Метод для получения вакансий из бд"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Метод для удаления вакансии из бд"""
        pass
