from abc import ABC, abstractmethod
import sqlite3




class Vacancy(ABC):
    connect = sqlite3.connect('./data/main.db', check_same_thread=False)
    cursor = connect.cursor()
    all_vacancies = []
    salary_from = 0
    salary_to = 0
    currency = 'RUR'

    @abstractmethod
    def insert_data(self):
        pass

    @abstractmethod
    def search_vacancy(self, query):
        pass

    @abstractmethod
    def delete_from_db(self):
        pass


class HHVacancy(Vacancy):

    def __init__(self, vacancy) -> None:
        self.platform = 'HeadHunter'
        self.vacancy_id = vacancy['id']
        self.title = vacancy['name']
        self.requirement = vacancy['snippet']['requirement']
        self.responsibility = vacancy['snippet']['responsibility']
        self.employer = vacancy['employer']['name']
        if vacancy.get('salary'):
            if vacancy.get('salary').get('from'):
                self.salary_from = vacancy.get('salary').get('from')
            if vacancy.get('salary').get('to'):
                self.salary_to = vacancy['salary']['to']
            self.currency = vacancy['salary']['currency']
        self.url = vacancy['alternate_url']
        self.all_vacancies.append(self)
    @classmethod
    def insert_data(cls) -> None:
        for vacancy in cls.all_vacancies:
            cls.cursor.execute(f"SELECT vacancy_id FROM vacancies WHERE vacancy_id = '{vacancy.vacancy_id}'")
            result = cls.cursor.fetchone()
            if not result:
                cls.cursor.execute('INSERT INTO vacancies (platform, vacancy_id, title, requirement, responsibility,'
                               'employer, salary_from, salary_to, currency, url) VALUES (?,?,?,?,?,?,?,?,?,?)',
                               (vacancy.platform, vacancy.vacancy_id, vacancy.title, vacancy.requirement,
                                vacancy.responsibility, vacancy.employer, vacancy.salary_from, vacancy.salary_to,
                                vacancy.currency, vacancy.url))
                cls.connect.commit()

    @classmethod
    def search_vacancy(cls, query):
        cls.cursor.execute(f"SELECT vacancy_id, title, salary_from FROM vacancies WHERE title LIKE '%{query}%' "
                           f"ORDER BY salary_from DESC")
        result = cls.cursor.fetchmany(3)
        return result

    def delete_from_db(self):
        pass

    def __str__(self):
        return f'{self.title}\n{self.salary_from}\n{self.salary_to}\n{self.currency}'


class SJVacancy(Vacancy):

    def insert_vacancy(self):
        pass

    def search_vacancy(self):
        pass

    def delete_from_db(self):
        pass