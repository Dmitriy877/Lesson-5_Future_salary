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
    it_vacancy_information = {}


    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    vacancies = response.json()["items"]

    for language in languages:
        payload = {"text": "Программист {0}".format(language),
                   "area": moscow_area_id,
                   "premium": True,
                   "only_with_salary": True
                   }
        response = requests.get("https://api.hh.ru/vacancies", params=payload)
        response.raise_for_status()
        it_vacancy_information.update({language: response.json()})
    print(it_vacancy_information)








    for vacancy in vacancies:
        print(predict_rub_salary(vacancy))


if __name__ == "__main__":
    main()
