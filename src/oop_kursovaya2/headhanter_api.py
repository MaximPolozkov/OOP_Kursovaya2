import requests

from src.oop_kursovaya2.vacancy_api import VacancyAPI


class HeadHanterAPI(VacancyAPI):
    """Класс для получения вакансий с hh"""
    def get_vacancies(self):
        url = f"https://api.hh.ru/vacancies"
        response = requests.get(url)
        return response.json()['items'] if response.status_code == 200 else []
