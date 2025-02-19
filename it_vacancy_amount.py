import requests


def it_vacancy_amount(payload):
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    return response.json()["found"]


def main():
    moscow_area_id = 1
    it_vacancy = {}
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

    for language in languages:
        payload = {"text": "Программист {0}".format(language),
                   "area": moscow_area_id,
                   "premium": True,
                   }
        it_vacancy.update({language: it_vacancy_amount(payload)})
    print(it_vacancy)


if __name__ == "__main__":
    main()

    # payload_it_vacancy_amount_moscow = {
    #                                     "text": "Программист",
    #                                     "area": moscow_area_id,
    #                                     "premium": True,
    #                                     }
    # payload_it_vacancy_amount_moscow_last_month = {
    #                                                "text": "Программист",
    #                                                "area": moscow_area_id,
    #                                                "premium": True,
    #                                                "date_from": "2025-01-17"
    #                                                }

    # it_vacancy_amount_moscow = it_vacancy_amount(payload_it_vacancy_amount_moscow)
    # it_vacancy_amount_moscow_last_month = it_vacancy_amount(payload_it_vacancy_amount_moscow_last_month)
    # print(
    #       "Количество вакансий на должность программисста в Москве: ",
    #       it_vacancy_amount_moscow
    #       )
    # print(
    #       "Количество вакансий на должность программиста в Москве за последний месяц: ", 
    #       it_vacancy_amount_moscow_last_month
    #       )
