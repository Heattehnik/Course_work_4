from abc import ABC, abstractmethod
import requests as req


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

    def get_vacancies(self) -> dict:
        self.response = req.get('https://api.hh.ru/vacancies')
        return self.response.json()


if __name__ == '__main__':
    connect = HeadHunterAPI()
    response = connect.get_vacancies()
    print(response)
