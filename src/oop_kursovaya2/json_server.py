import json
from typing import Dict, Any, Optional, List

from src.oop_kursovaya2.headhanter_api import HeadHanterAPI
from src.oop_kursovaya2.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename="vacancies.json"):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """Добавляет вакансии в JSON-файл"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                data = list(json.load(f))
        except FileNotFoundError:
            print("файл не найден")
            data = []
        except json.JSONDecodeError:
            data = []

        data.append(vacancy)

        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, criteria: Optional[str] = None) -> List[Dict[str, Any]]:
        """Получает вакансии из JSON-файла пи критериям"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if criteria:
                filtered_vacancies = [
                    v for v in data
                    if (v.get('currency') and criteria.lower() in v['currency'].lower()) or (v.get('name') and criteria.lower() in v['name'].lower())
                ]
                return filtered_vacancies
            else:
                return data

        except FileNotFoundError:
            print("Файл не найден")
            return []
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON файла.")
            return []

    def delete_vacancy(self, name, url) -> None:
        """Удаляет вакансии из JSON-файла"""
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Файл не найден. Нечего удалять")
            return
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON. Файл поврежден")
            return

        delete_vacancies = [
            v for v in data
            if (v.get('name') != name and
                v.get('url') != url
                )
        ]

        try:
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(delete_vacancies, f, indent=4, ensure_ascii=False)
            print("Вакансия успешно удалена.")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")


if __name__ == "__main__":
    hh_api = HeadHanterAPI()
    vacancies = hh_api.get_vacancies()
    json_server = JSONSaver()
    for vacancy_data in vacancies:
        vacancy = Vacancy(
            name=vacancy_data.get('name'),
            city=vacancy_data.get('area', {}).get('name') if vacancy_data.get('area') else None,
            # Добавил проверку на None
            url=vacancy_data.get('alternate_url'),  # Исправил на alternate_url
            salary_from=vacancy_data.get('salary', {}).get('from') if vacancy_data.get('salary') else None,
            # Добавил проверку
            salary_to=vacancy_data.get('salary', {}).get('to') if vacancy_data.get('salary') else None,
            # Добавил проверку
            currency=vacancy_data.get('salary', {}).get('currency') if vacancy_data.get('salary') else None
            # Добавил проверку
        )
        json_server.add_vacancy(vacancy.to_dict())

    all_vacancies = json_server.get_vacancies("Комплектовщик на склад Золотое Яблоко")
    print(all_vacancies)


