import requests


def it_vacancy_amount(vacancy_name, area_id, period=""):
    if not period:
        payload = {
                  "text": vacancy_name,
                  "area": area_id,
                  "premium": True,
                  }
    else:
        payload = {
                  "text": vacancy_name,
                  "area": area_id,
                  "premium": True,
                  "period": period
                  }
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    return response.json()["found"]


def main():
    moscow_area_id = 1
    it_vacancy_amount_moscow = it_vacancy_amount(
                                           "Программист",
                                           moscow_area_id,
                                           )
    it_vacancy_amount_moscow_last_month = it_vacancy_amount(
                                           "Программист",
                                           moscow_area_id,
                                           "2025-01-17"
                                           )
    print(
          "Количество вакансий на должность программисста в Москве: ",
          it_vacancy_amount_moscow
          )
    print(
          "Количество вакансий на должность программиста в Москве за последний месяц: ", 
          it_vacancy_amount_moscow_last_month
          )


if __name__ == "__main__":
    main()


# import requests


# def it_vacancy_amount(vacancy_name, area_id, date_from=""):
#     payload = {
#               "text": vacancy_name,
#               "area": area_id,
#               "premium": True,
#               "date_from": date_from
#               }
#     response = requests.get("https://api.hh.ru/vacancies", params=payload)
#     response.raise_for_status()
#     return response.json()["found"]


# def main():
#     moscow_area_id = 1
#     it_vacancy_amount_moscow = it_vacancy_amount(
#                                            "Программист",
#                                            moscow_area_id,
#                                            )
#     it_vacancy_amount_moscow_last_month = it_vacancy_amount(
#                                            "Программист",
#                                            moscow_area_id,
#                                            "2025-01-17"
#                                            )
#     print(
#           "Количество вакансий на должность программисста в Москве: ",
#           it_vacancy_amount_moscow
#           )
#     print(
#           "Количество вакансий на должность программиста в Москве за последний месяц: ", 
#           it_vacancy_amount_moscow_last_month
#           )


# if __name__ == "__main__":
#     main()

