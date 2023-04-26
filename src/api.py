from abc import ABC, abstractmethod
import requests as req
from dotenv import load_dotenv
import os

load_dotenv()


class APIConnector(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(APIConnector):

    def __init__(self):
        self.response = None

    def get_vacancies(self) -> dict:
        self.response = req.get('https://api.hh.ru/vacancies')
        return self.response.json()


class SuperJobAPI(APIConnector):

    def __init__(self):
        self.response = None
        self.token = os.getenv('SJ_TOKEN')
        self.client_id = os.getenv('SJ_CLIENT_ID')
        self.headers = {'X-Api-App-Id': self.token}
    def get_vacancies(self) -> dict:
        keywords = ['python developer']
        self.response = req.get(f'https://api.superjob.ru/2.0/vacancies/?keywords={keywords}&count=100&page=1&published=3&archive=1',
                                headers=self.headers)
        return self.response.json()


if __name__ == '__main__':
    connect = SuperJobAPI()
    response = connect.get_vacancies()
    print(response)
