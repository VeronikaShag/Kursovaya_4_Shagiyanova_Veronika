

class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, description):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description

    def __str__(self):
        return f"""Название вакансии: {self.name}
Ссылка: {self.url}
З/П: от {self.salary_from} до {self.salary_to}
"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from
