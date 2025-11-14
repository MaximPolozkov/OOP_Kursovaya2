from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List


class DataServer(ABC):
    """Абстрактный метод для записи данных в бд"""
    @abstractmethod
    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """Метод для добавления вакансии в бд"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[str] = None) -> List[Dict[str, Any]]:
        """Метод для получения вакансий из бд"""
        pass

    @abstractmethod
    def delete_vacancy(self, name: str, url: str) -> None:
        """Метод для удаления вакансии из бд"""
        pass
