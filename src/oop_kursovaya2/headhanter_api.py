from typing import Any, Optional, Dict, List

import requests

from src.oop_kursovaya2.vacancy_api import VacancyAPI


class HeadHanterAPI(VacancyAPI):
    """Класс для получения вакансий с hh"""

    def __init__(self, text):
        self.__url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': text, 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self) -> Optional[List[Dict[str, Any]]]:
        """Приватный метод для подключения к API"""
        try:
            while self.params.get('page') < 20:
                response = requests.get(self.__url, headers=self.headers, params=self.params)
                response.raise_for_status()
                vacancie = response.json()['items']
                self.vacancies.extend(vacancie)
                self.params['page'] += 1
                #return self.vacancies
            return self.vacancies
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None

    def get_vacancies(self, query: str = None, page: int = 0) -> List[Dict[str, Any]]:
        """Получает вакансии с hh.ru с учетом пагинации."""
        params = {'text': query, 'page': page, 'per_page': 100} if query else {'page': page, 'per_page': 100}  # Добавил параметры для пагинации
        data = self._connect(params)
        return data.get('items', []) if data else []

    def get_all_vacancies(self, query: str = None) -> List[Dict[str, Any]]:
        """Получает все вакансии по запросу, перебирая страницы."""
        all_vacancies = []
        page = 0
        while True:
            params = {'text': query, 'page': page, 'per_page': 100} if query else {'page': page, 'per_page': 100}
            data = self._connect(params)  # Получаем данные с текущей страницы
            if not data or 'items' not in data or not data['items']:
                break

            all_vacancies.extend(data['items'])
            page += 1

        return all_vacancies
