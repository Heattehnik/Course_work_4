from abc import ABC, abstractmethod
import sqlite3


class Vacancy(ABC):
    """
    Абстрактный класс для работы с вакансиями и взаимодействия с базой данных

    """
    connect = sqlite3.connect('./data/main.db', check_same_thread=False)
    cursor = connect.cursor()
    all_vacancies = []
    salary_from = 0
    salary_to = 0
    currency = 'RUR'

    @abstractmethod
    def insert_data(self) -> None:
        pass

    @abstractmethod
    def search_vacancy(self, query: str, count: str = 5):
        pass

    @abstractmethod
    def delete_from_db(self) -> None:
        pass


class HHVacancy(Vacancy):
    """
    Класс для обработки вакансий полученных с hh.ru
    """

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
        """
        Метод класса для записи полученных вакансий в базу данных
        """
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
    def search_vacancy(cls, query: str, count: int = 5) -> list[tuple]:
        """
        Метод для получения вакансий из базы данных по запросу пользователя.
        :param query: Строка запроса
        :param count: Количество возвращаемых вакансий
        :return: Список кортежей с вакансиями отсортированных по уменьшению зарплаты.
        """
        cls.cursor.execute(f"SELECT vacancy_id, title, salary_from FROM vacancies WHERE title LIKE '%{query}%' "
                           f"ORDER BY salary_from DESC")
        result = cls.cursor.fetchmany(count)
        return result

    def delete_from_db(self) -> None:
        """
        Метод для удаления вакансии
        :return:
        """
        pass

    def __str__(self) -> str:
        return f'{self.title}\n{self.salary_from}\n{self.salary_to}\n{self.currency}'


class SJVacancy(Vacancy):
    """
    Класс для обработки вакансий полученных с superjob.ru
    """

    def __init__(self, vacancy) -> None:
        self.platform = 'SuperJob'
        self.vacancy_id = vacancy['id']
        self.title = vacancy['profession']
        self.requirement = vacancy['candidat']
        self.employer = vacancy['firm_name']
        if vacancy.get('payment_from'):
            self.salary_from = vacancy['payment_from']
        if vacancy.get('payment_to'):
            self.salary_to = vacancy['payment_to']
        self.currency = vacancy['currency']
        self.url = vacancy['link']
        self.all_vacancies.append(self)

    @classmethod
    def insert_data(cls) -> None:
        """
        Метод класса для записи полученных вакансий в базу данных
        """
        for vacancy in cls.all_vacancies:
            cls.cursor.execute(f"SELECT vacancy_id FROM vacancies WHERE vacancy_id = '{vacancy.vacancy_id}'")
            result = cls.cursor.fetchone()
            if not result:
                cls.cursor.execute('INSERT INTO vacancies (platform, vacancy_id, title, requirement,'
                                   'employer, salary_from, salary_to, currency, url) VALUES (?,?,?,?,?,?,?,?,?)',
                                   (vacancy.platform, vacancy.vacancy_id, vacancy.title, vacancy.requirement,
                                    vacancy.employer, vacancy.salary_from, vacancy.salary_to,
                                    vacancy.currency, vacancy.url))
                cls.connect.commit()

    @classmethod
    def search_vacancy(cls, query: str, count: int = 5) -> list[tuple]:
        """
        Метод для получения вакансий из базы данных по запросу пользователя.
        :param query: Строка запроса
        :param count: Количество возвращаемых вакансий
        :return: Список кортежей с вакансиями отсортированных по уменьшению зарплаты.
        """
        cls.cursor.execute(f"SELECT vacancy_id, title, salary_from FROM vacancies WHERE title LIKE '%{query}%' "
                           f"ORDER BY salary_from DESC")
        result = cls.cursor.fetchmany(count)
        return result

    def delete_from_db(self):
        pass
