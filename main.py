from src.api import HeadHunterAPI, SuperJobAPI
from src.vacancies import HHVacancy, SJVacancy


def user_interact():
    headhunter = HeadHunterAPI()
    headhunter.get_vacancies('Python')
    headhunter.add_vacancies()
    HHVacancy.insert_data()
    superjob = SuperJobAPI()
    superjob.get_vacancies('Python')
    superjob.add_vacancies()
    SJVacancy.insert_data()
    # some = HHVacancy.search_vacancy('Python')
    # for i in some:
    #     print(i)

