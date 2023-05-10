from abc import ABC, abstractmethod
import requests as req
from dotenv import load_dotenv
import json
import os
import time

load_dotenv()


class APIConnector(ABC):

    @abstractmethod
    def get_vacancies(self, keywords):
        pass

    @abstractmethod
    def make_file(self):
        pass


class HeadHunterAPI(APIConnector):
    vacancies = []
    def __init__(self):
        self.response = None

    def get_vacancies(self, keywords: str) -> None:
        self.response = req.get(f'https://api.hh.ru/vacancies?area=113&text={keywords}&per_page=100')
        self.response.content.decode()
        self.vacancies.append(self.response.json())
        if self.response.json().get('pages') > 1:
            for page in range(1, self.response.json().get('pages')):
                response = req.get(f'https://api.hh.ru/vacancies?area=113&text={keywords}&per_page=100&page={page}')
                response.content.decode()
                self.vacancies.append(response.json())

    def make_file(self) -> None:
        for page in self.vacancies:
            with open('hh_vacancies.json', 'a+', encoding='utf-8') as file:
                file.write(json.dumps(page, indent=2, ensure_ascii=False))


class SuperJobAPI(APIConnector):
    vacancies = []
    token = os.getenv('SJ_TOKEN')
    client_id = os.getenv('SJ_CLIENT_ID')
    headers = {'X-Api-App-Id': token}

    def __init__(self):
        self.response = None

    def get_vacancies(self, keywords) -> list:
        keywords = keywords
        temp = {'more': True}
        page = 1
        while temp.get('more'):
            if page == 119:
                time.sleep(60)
            self.response = req.get(f'https://api.superjob.ru/2.0/vacancies/?keywords={keywords}&not_archive=1&count=50&page={page}',
                                    headers=self.headers)
            self.vacancies.append(self.response.json())
            temp['more'] = self.response.json().get('more')
            page += 1
        return self.vacancies

    def make_file(self) -> None:
        for page in self.vacancies:
            with open('sj_vacancies.json', 'a+', encoding='utf-8') as file:
                file.write(json.dumps(page, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    headhunter = HeadHunterAPI()
    headhunter.get_vacancies('Python')
    headhunter.make_file()
    superjob = SuperJobAPI()
    superjob.get_vacancies('Python')
    superjob.make_file()
    # print(len(response))
    # with open('vacancies.json', 'w', encoding='utf-8') as file:
    #     i = 0
    #     for vacancie in response:
    #         for item in vacancie['objects']:
    #             file.write(f"{item.get('id')}\n{item.get('profession')}\n{i}\n")
    #             i += 1
    #     # f.write(json.dumps(data, sort_keys=True, ensure_ascii=False))
