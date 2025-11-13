import requests
import unittest
from unittest.mock import patch

from src.oop_kursovaya2.headhanter_api import HeadHanterAPI


class TestHeadHanterAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        # Мокаем запрос и его результат
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': [{'title': 'Python Developer', 'company': 'Tech Corp'}]}

        # Создаем экземпляр класса для тестирования
        hh_api = HeadHanterAPI()

        # Вызываем метод и проверяем результат
        vacancies = hh_api.get_vacancies()

        # Проверяем, что метод вернул ожидаемый результат
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]["title"], "Python Developer")
        self.assertEqual(vacancies[0]["company"], "Tech Corp")

    @patch('requests.get')
    def test_get_vacancies_failure(self, mock_get):
        # Мокаем запрос, возвращаем ошибочный статус
        mock_get.return_value.status_code = 404

        hh_api = HeadHanterAPI()
        vacancies = hh_api.get_vacancies()

        # Проверяем, что при ошибке статуса метод возвращает пустой список
        self.assertEqual(vacancies, [])
