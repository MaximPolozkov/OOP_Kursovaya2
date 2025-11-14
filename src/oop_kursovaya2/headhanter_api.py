from typing import Any, Optional, Dict, List

import requests

from src.oop_kursovaya2.vacancy_api import VacancyAPI


class HeadHanterAPI(VacancyAPI):
    """Класс для получения вакансий с hh"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def _connect(self) -> Optional[Dict]:
        """Приватный метод для подключения к API"""
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None

    def get_vacancies(self) -> List[Dict[str, Any]]:
        """Получает вакансии с hh.ru"""
        data = self._connect()
        return data.get('items', []) if data else []
