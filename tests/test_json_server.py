import json


def test_add_vacancy(json_saver, vacancy):
    """Тест для создании вакансии в JSON файле"""
    json_saver.add_vacancy(vacancy.to_dict())
    with open(json_saver.filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['name'] == "Python Developer"


def test_get_vacancies(json_saver, vacancy):
    """Тест для получения вакансии по критериям"""
    json_saver.add_vacancy(vacancy.to_dict())
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]['city'] == "Moscow"


def test_get_vacancies_with_criteria(json_saver, vacancy):
    """Тест для получения вакансии, критерии не найдены"""
    json_saver.add_vacancy(vacancy.to_dict())
    vacancies = json_saver.get_vacancies(criteria="Python")
    assert len(vacancies) == 1
    vacancies = json_saver.get_vacancies(criteria="USD")
    assert len(vacancies) == 0


def test_delete_vacancy(json_saver, vacancy):
    """Удаление вакансии из JSON файла"""
    json_saver.add_vacancy(vacancy.to_dict())
    json_saver.delete_vacancy("Python Developer", "http://example.com")
    with open(json_saver.filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data) == 0
