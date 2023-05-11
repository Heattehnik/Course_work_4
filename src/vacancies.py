from abc import ABC, abstractmethod
import sqlite3

connect = sqlite3.connect('../data/main.db', check_same_thread=False)
cursor = connect.cursor()


class Vacancy(ABC):
    all_vacancies = []

    def __init__(self, platform, vacancy_id, title, description, salary_from, salary_to, employer, url) -> None:
        self.platform = platform
        self.vacancy_id = vacancy_id
        self.title = title
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.url = url
        self.all_vacancies.append(self)

    @abstractmethod
    def insert_vacancy(self):
        pass

    @abstractmethod
    def search_vacancy(self):
        pass

    @abstractmethod
    def delete_from_db(self):
        pass


class HHVacancy(Vacancy):

    def insert_vacancy(self):
        pass

    def search_vacancy(self):
        pass

    def delete_from_db(self):
        pass


class SJVacancy(Vacancy):

    def insert_vacancy(self):
        pass

    def search_vacancy(self):
        pass

    def delete_from_db(self):
        pass