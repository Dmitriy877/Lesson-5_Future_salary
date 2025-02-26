from dotenv import load_dotenv
import os
import requests
import pprint


def get_professions(api_key, payload):
    professions = []
    headers = {"X-Api-App-Id": api_key}
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    for vacancy in response.json()["objects"]:
        professions.append(vacancy)
    return professions


def get_professions_with_city(api_key, payload):
    professions_with_city = []
    headers = {"X-Api-App-Id": api_key}
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    for vacancy in response.json()["objects"]:
        professions_with_city.append(f"{vacancy["profession"]}, {vacancy["town"]["title"]}")
    return professions_with_city


def get_professions_city_salary(api_key, payload):
    professions_with_city = []
    headers = {"X-Api-App-Id": api_key}
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    for vacancy in response.json()["objects"]:
        vacancy_profession = vacancy["profession"]
        vacancy_city = vacancy["town"]["title"]
        vacancy_payments = predict_rub_salary_super_job(vacancy)
        professions_with_city.append(f"{vacancy_profession}, {vacancy_city}, {vacancy_payments}")
    return professions_with_city


def predict_rub_salary_super_job(vacancy):
    if vacancy["payment_from"] and vacancy["payment_to"]:
        return (vacancy["payment_from"] + vacancy["payment_to"])/2
    if not vacancy["payment_from"] and vacancy["payment_to"]:
        return vacancy["payment_to"]*0.8
    if vacancy["payment_from"] and not vacancy["payment_to"]:
        return vacancy["payment_from"]*1.2


def main():

    load_dotenv()
    SUPER_JOB_SECRET_KEY = os.environ["SUPER_JOB_SECRET_KEY"]

    payload_super_job = {
               "period": 0,
               "town": "Москва",
               "catalogues": 48,
               }

    professions = get_professions_city_salary(SUPER_JOB_SECRET_KEY, payload_super_job)
    pprint.pprint(professions)


if __name__ == "__main__":
    main()
