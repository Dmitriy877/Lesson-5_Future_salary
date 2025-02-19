import requests


def it_vacancy_amount(payload):
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    return response.json()["found"]


def main():
    moscow_area_id = 1
    vacancy_salary = []
    payload = {"text": "Программист Python",
               "area": moscow_area_id,
               "premium": True,
               "only_with_salary": True
               }
    response = requests.get("https://api.hh.ru/vacancies", params=payload)
    response.raise_for_status()
    vacancies = response.json()["items"]

    for vacancy in vacancies:
        vacancy_salary.append(vacancy["salary"])
    print(vacancy_salary)


if __name__ == "__main__":
    main()
