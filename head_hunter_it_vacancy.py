import requests
import pprint


# "headhunter"

def get_it_vacancy_found(payload):
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    vacancy_found = response.json()["found"]
    return vacancy_found


def predict_rub_salary(vacancy):
    if vacancy["salary"]["from"] and vacancy["salary"]["to"]:
        return (vacancy["salary"]["from"] + vacancy["salary"]["to"])/2
    if not vacancy["salary"]["from"] and vacancy["salary"]["to"]:
        return vacancy["salary"]["to"]*0.8
    if vacancy["salary"]["from"] and not vacancy["salary"]["to"]:
        return vacancy["salary"]["from"]*1.2


def get_only_salary(payload):
    it_vacancies = fetch_it_vacancy_info(payload)
    only_salary = []
    for vacancy in it_vacancies:
        only_salary.append(predict_rub_salary(vacancy))
    return only_salary


def get_page_amount(payload):
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    pages_amount = response.json()["pages"]
    return pages_amount


def fetch_it_vacancy_info(payload):
    it_vacancies = []
    page = 0
    pages_amount = get_page_amount(payload)

    while page < pages_amount:
        payload.update({"page": page})
        page_response = requests.get("https://api.hh.ru/vacancies", params=payload)
        page_response.raise_for_status()
        for vacancy in page_response.json()["items"]:
            it_vacancies.append(vacancy)

        page += 1

    return it_vacancies


def get_it_sphere_info(languages, area_id):
    salary_information = {}
    for language in languages:
        payload = {"text": "Программист {0}".format(language),
                   "area": area_id,
                   "premium": True,
                   "only_with_salary": True,
                   }

        only_salary = get_only_salary(payload)
        vacancy_found = get_it_vacancy_found(payload)
        processed_salary = len(only_salary)
        average_salary = int((sum(only_salary)/len(only_salary)))
        salary_information.update({language: {"vacancy_found": vacancy_found,
                                              "processed_salary": processed_salary,
                                              "average_salary": average_salary,
                                              }})
    return salary_information

# superjob


def main():
    hh_area_id_moscow = 1
    languages = [
                 "JavaScript",
                 "Java",
                 "Python",
                 "Ruby",
                 "PHP",
                 "C++",
                 "CSS",
                 "C#",
                 "C",
                 "GO",
                 "Shell",
                 "Objective-C",
                 "Scala",
                 "Swift",
                 "TypeScript",
    ]
    pprint.pprint(get_it_sphere_info(languages, hh_area_id_moscow))


if __name__ == "__main__":
    main()
