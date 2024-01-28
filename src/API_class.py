from abc import ABC, abstractmethod
import requests

from config import API_KEY_SJ


class AbstractAPI(ABC):

    @abstractmethod
    def get_vacancies(self, text):
        pass

    @abstractmethod
    def filter_vacancies(self, text):
        pass


class SuperJob(AbstractAPI):

    def get_vacancies(self, text):
        headers = {'X-Api-App-Id': API_KEY_SJ}
        params = {"keyword": text}
        vacancies = requests.get("	https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()
        return vacancies['objects']

    def filter_vacancies(self, text):
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({
                "name": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": vacancy["payment_from"],
                "salary_to": vacancy["payment_to"],
                "description": vacancy["candidat"]
            })
        return vacancies_filter


class HH_class(AbstractAPI):

    def get_vacancies(self, text):
        params = {"text": text, "area": 1}
        vacancies = requests.get("https://api.hh.ru/vacancies", params=params).json()
        return vacancies['items']

    def filter_vacancies(self, text):
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            salary = vacancy['salary']
            if not salary:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = salary['from']
                salary_to = salary['to']
                if not salary_from:
                    salary_from = 0
                if not salary_to:
                    salary_to = 0
            vacancies_filter.append({
                "name": vacancy["name"],
                "url": vacancy["url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "description": vacancy["snippet"]["responsibility"]
            })
        return vacancies_filter
