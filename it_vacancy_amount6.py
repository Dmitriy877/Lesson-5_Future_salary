import requests


def it_vacancy_amount(payload):
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    return response.json()["found"]


def predict_rub_salary(vacancy):
    if vacancy["salary"]["from"] and vacancy["salary"]["to"]:
        return (vacancy["salary"]["from"] + vacancy["salary"]["to"])/2
    if not vacancy["salary"]["from"] and vacancy["salary"]["to"]:
        return vacancy["salary"]["to"]*0.8
    if vacancy["salary"]["from"] and not vacancy["salary"]["to"]:
        return vacancy["salary"]["from"]*1.2


def main():
    moscow_area_id = 1
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
    it_vacancy_spheres = {}
    salary_infromation = {}
    vacancies_salary = []

    for language in languages:
        payload = {"text": "Программист {0}".format(language),
                   "area": moscow_area_id,
                   "premium": True,
                   "only_with_salary": True
                   }
        response = requests.get("https://api.hh.ru/vacancies", params=payload)
        response.raise_for_status()
        page = 0
        pages_number = response.json()["pages"]

        it_vacancy_spheres.update({language: {}})

        while page < pages_number:
            payload = {"text": "Программист {0}".format(language),
                   "area": moscow_area_id,
                   "premium": True,
                   "only_with_salary": True,
                   "page": page
                   }

            page_response = requests.get("https://api.hh.ru/vacancies", params=payload)
            page_response.raise_for_status()

            page_payload = page_response.json()
            it_vacancy_spheres[language].update(page_payload)
            print(it_vacancy_spheres)
            page += 1

    # for language in it_vacancy_spheres:

    #     for vacancy in it_vacancy_spheres[language]["items"]:
    #         vacancies_salary.append(predict_rub_salary(vacancy))

    #     vacancies_found = it_vacancy_spheres[language]["found"]
    #     vacancies_processed = len(it_vacancy_spheres[language])
    #     average_salary = int(sum(vacancies_salary)/len(vacancies_salary))
    #     salary_infromation.update({language: {"vacancies_found": vacancies_found,
    #                                           "vacancies_processed": vacancies_processed,
    #                                           "average_salary": average_salary
    #                                           }})

    # print(salary_infromation)


if __name__ == "__main__":
    main()
