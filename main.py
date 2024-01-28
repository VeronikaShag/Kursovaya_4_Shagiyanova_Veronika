from src.API_class import SuperJob, HH_class
from src.json_saver import JSONSaver

if __name__ == '__main__':
    platform = input('Выберите на каких платформах производить поиск: \n'
                     '1 - HeadHunter\n'
                     '2 - SuperJob\n'
                     '3 - HeadHunter и SuperJob\n')

    if platform == '1':
        hh = HH_class()
        json_saver = JSONSaver("vacancies.json")
        keyword = input('Введите ключевое слово для поиска вакансий: ')
        vacancies = hh.filter_vacancies(keyword)
        json_saver.write_vacancies(vacancies)
        list_vacancies_ex = json_saver.read_vacancies()
    elif platform == '2':
        sj = SuperJob()
        json_saver = JSONSaver("vacancies.json")
        keyword = input('Введите ключевое слово для поиска вакансий: ')
        vacancies = sj.filter_vacancies(keyword)
        json_saver.write_vacancies(vacancies)
        list_vacancies_ex = json_saver.read_vacancies()
    elif platform == '3':
        hh = HH_class()
        sj = SuperJob()
        json_saver = JSONSaver("vacancies.json")
        keyword = input('Введите ключевое слово для поиска вакансий: ')
        vacancies = hh.filter_vacancies(keyword) + sj.filter_vacancies(keyword)
        json_saver.write_vacancies(vacancies)
        list_vacancies_ex = json_saver.read_vacancies()

    conclusion = input('Выберите в каком виде вывести список вакансий:\n'
                       '1 - все найденный вакансии\n'
                       '2 - по возрастанию зарплаты\n'
                       '3 - по убыванию зарплаты\n'
                       '4 - ТОП-N вакансий по зарплате (необходимо ввести N)\n')

    if conclusion == '1':
        # вывод всех вакансий
        for vacancy in list_vacancies_ex:
            print(vacancy)
            print("-" * 50)

    elif conclusion == '2':
        # сортировка по зп возрастание
        for vacancy in sorted(list_vacancies_ex):
            print(vacancy)
            print("-" * 50)

    elif conclusion == '3':
        # сортировка по зп нисходящая
        for vacancy in sorted(list_vacancies_ex, reverse=True):
            print(vacancy)
            print("-" * 50)

    elif conclusion == '4':
        # ТОП вакансий
        quantity = int(input('Введите число вакансий: '))
        vacancy_list = []
        for vacancy in sorted(list_vacancies_ex, reverse=True):
            vacancy_list.append(vacancy)

        for vacancy in vacancy_list[:quantity]:
            print(vacancy)
            print("-" * 50)
