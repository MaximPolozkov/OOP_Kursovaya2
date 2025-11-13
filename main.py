from src.oop_kursovaya2.vacancy import Vacancy
from src.oop_kursovaya2.headhanter_api import HeadHanterAPI
from src.oop_kursovaya2.json_server import JSONSaver

def user_interaction():
    """Функция для взаимодействия с пользователем"""
    # hh_api = HeadHanterAPI()
    # json_saver = JSONSaver()

    while True:
        print("\n1. Поиск вакансий на hh.ru")
        print("2. Вывести вакансии из файла")
        print("3. Удалить вакансию")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
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
                json_server.add_vacancy(vacancy)  # Добавляем созданный объект Vacancy

            job_search = input("Введите вакансию: ")
            all_vacancies = json_server.get_vacancies(job_search)
            print(all_vacancies)


        elif choice == '2':
            criteria = input("Введите ключевое слово для фильтрации (или нажмите Enter для вывода всех): ")
            json_server = JSONSaver()
            vacancies = json_server.get_vacancies(criteria) #получаем список вакансий
            if vacancies:
                top_n = input("Введите количество вакансий для вывода в топе: ")
                try:
                    top_n = int(top_n)
                except ValueError:
                    print("Некорректный ввод. Будут выведены все вакансии.")
                    top_n = len(vacancies)

                sorted_vacancies = sorted(
                    vacancies,
                    key=lambda x: x.get('salary_from') or 0,
                    reverse=True)  # сортируем по зарплате

                for i, vacancy in enumerate(sorted_vacancies[:top_n]):
                    print(f"{i+1}. {vacancy}")
            else:
                print("Нет вакансий, соответствующих критериям.")

        elif choice == '3':
            name = input("Введите название вакансии для удаления: ")
            url = input("Введите url вакансии для удаления: ")
            # salary_from = int(input("Введите минимальную зарплату вакансии для удаления: "))
            # salary_to = int(input("Введите максимальную зарплату вакансии для удаления: "))
            # requirement = input("Введите описание вакансии для удаления: ")

            #vacancy_to_delete = Vacancy(name, url)  # создаём экземпляр вакансии

            json_server = JSONSaver()
            json_server.delete_vacancy(name, url)
            print("Вакансия удалена.")

        elif choice == '4':
            break #выйти из цикла

        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    user_interaction()
