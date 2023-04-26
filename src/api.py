from abc import ABC, abstractmethod
import requests as req


class APIConnector(ABC):

    @abstractmethod
    def connect(self):
        pass


class HeadHunterAPI(APIConnector):

    def __init__(self):
        pass

    def connect(self):
        response = req.get()
        pass


class SuperJobAPI(APIConnector):

    def connect(self):
        response = req.get()
        pass
