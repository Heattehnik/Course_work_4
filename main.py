from src.api import HeadHunterAPI, SuperJobAPI

headhunter = HeadHunterAPI()
headhunter.get_vacancies('Python')
headhunter.make_file()
superjob = SuperJobAPI()
superjob.get_vacancies('Python')
superjob.make_file()
