from src.api import HeadHunterAPI, SuperJobAPI
from src.vacancies import HHVacancy

headhunter = HeadHunterAPI()
headhunter.get_vacancies('Python')
headhunter.make_file()
# superjob = SuperJobAPI()
# superjob.get_vacancies('Python')
# superjob.make_file()
headhunter.add_vacancies()
HHVacancy.insert_data()
some = HHVacancy.search_vacancy('Python')
for i in some:
    print(i)

