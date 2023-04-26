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

    def get_vacancies(self) -> dict:
        self.response = req.get('https://api.superjob.ru/2.0/vacancies/?keyword=%D0%91%D1%83%D1%85%D0%B3%D0%B0%D0%BB%D1%82%D0%B5%D1%80&order_field=payment&order_direction=asc&payment_from=10000&payment_to=300000&no_agreement=1&town=4&catalogues=33%2C151%2C11%2C438%2C327%2C306%2C478%2C86&place_of_work=1&moveable=1&agency=1&type_of_work=6&age=30&gender=2&education=2&experience=3&driving_licence%5B0%5D=B&driving_licence%5B1%5D=C&language=1&lang_level=3&languages_particular=1')
        return self.response.json()


if __name__ == '__main__':
    connect = SuperJobAPI()
    response = connect.get_vacancies()
    print(response)
