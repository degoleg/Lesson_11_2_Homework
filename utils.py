import json

def load_candidates_from_json():
    """
    Функция загружает всех кандидатов из файла candidates.json
    :param path:
    :return:
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_candidates_all():
    """
    Функция возвращает список всех кандидатов
    :return:
    """
    return load_candidates_from_json()


def get_candidate(candidate_id):
    """
    Функция возвращает одного кандидата по его id
    :param candidate_id:
    :return:
    """
    for candidate in get_candidates_all():
        if candidate['id'] == candidate_id:
            return candidate
    return 'Not Found'

def get_candidates_by_name(candidate_name):
    """
    Функция возвращает кандидатов по имени
    :param candidate_name:
    :return:
    """

def get_candidates_by_skill(skill_name):
    """
    Функция возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """



