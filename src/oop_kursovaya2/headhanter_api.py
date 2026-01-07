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
            return self.vacancies
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None

    def get_vacancies(self) -> List[Dict[str, Any]]:
        vacancies = self.load_vacancies()
        return vacancies if vacancies is not None else []
