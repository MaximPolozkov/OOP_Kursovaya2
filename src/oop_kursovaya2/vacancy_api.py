from abc import ABC, abstractmethod
from typing import Dict, Any, List


class VacancyAPI(ABC):
    """Абстрактный метод для работы с вакансиями API"""
    @abstractmethod
    def get_vacancies(self) -> List[Dict[str, Any]]:
        pass
