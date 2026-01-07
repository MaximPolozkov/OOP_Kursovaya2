import unittest
from unittest.mock import patch

import requests

from src.oop_kursovaya2.headhanter_api import HeadHanterAPI


class TestHeadHanterAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        """Мокаем запрос и его результат"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': [{'title': 'Python Developer', 'company': 'Tech Corp'}]}

        hh_api = HeadHanterAPI("Python")

        vacancies = hh_api.get_vacancies()

        self.assertEqual(len(vacancies), 20)
        self.assertEqual(vacancies[0]["title"], "Python Developer")
        self.assertEqual(vacancies[0]["company"], "Tech Corp")

    @patch('requests.get')
    def test_get_vacancies_failure(self, mock_get):
        """Мокаем запрос, возвращаем ошибочный статус"""
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Ошибка 404")

        hh_api = HeadHanterAPI("Python")
        vacancies = hh_api.get_vacancies()

        self.assertEqual(vacancies, [])
