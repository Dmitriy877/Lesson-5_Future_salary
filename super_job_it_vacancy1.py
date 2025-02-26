from dotenv import load_dotenv
import os
import requests
import pprint


def get_professions_city_salary(api_key, payload):
    professions_city_salary = []
    headers = {"X-Api-App-Id": api_key}
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    for vacancy in response.json()["objects"]:
        vacancy_profession = vacancy["profession"]
        vacancy_city = vacancy["town"]["title"]
        vacancy_payments = predict_rub_salary_super_job(vacancy)
        professions_city_salary.append(f"{vacancy_profession}, {vacancy_city}, {vacancy_payments}")
    return professions_city_salary


def predict_rub_salary_super_job(vacancy):
    if vacancy["payment_from"] and vacancy["payment_to"]:
        return (vacancy["payment_from"] + vacancy["payment_to"])/2
    if not vacancy["payment_from"] and vacancy["payment_to"]:
        return vacancy["payment_to"]*0.8
    if vacancy["payment_from"] and not vacancy["payment_to"]:
        return vacancy["payment_from"]*1.2

def get

# def get_super_job_vacancy(languages, api_key):
#     for language in languages:
#         payload_super_job = {
#                "period": 0,
#                "town": "Москва",
#                "catalogues": 48,
#                "currency": "rub"
#                }



def main():

    load_dotenv()
    SUPER_JOB_SECRET_KEY = os.environ["SUPER_JOB_SECRET_KEY"]

    payload_super_job = {
               "period": 0,
               "town": "Москва",
               "catalogues": 48,
               "currency": "rub"
               }

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

    


    professions = get_professions_city_salary(SUPER_JOB_SECRET_KEY, payload_super_job)
    pprint.pprint(professions)


if __name__ == "__main__":
    main()
