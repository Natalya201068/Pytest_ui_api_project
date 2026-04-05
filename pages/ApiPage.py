import requests
from dotenv import load_dotenv
import os
import allure
load_dotenv()


class ApiPage:
    def __init__(self, url: str) -> None:
        self.url = url or os.getenv("URL")
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": os.getenv("X_API_KEY")
        }

    @allure.step('Найти фильм по названию {film_query}')
    def get_film_with_query(self, film_query: str) -> tuple:
        full_url = (f"{self.url}v1.4/movie/search?page=1&limit=10"
                    f"&query={film_query}")
        response = requests.get(full_url, headers=self.headers)
        status_code = response.status_code
        film_name = response.json()
        return status_code, film_name

    @allure.step('Найти фильм по {film_id}')
    def get_film_with_id(self, film_id: int) -> tuple:
        full_url = f"{self.url}v1.4/movie/{film_id}"
        response = requests.get(full_url, headers=self.headers)
        status_code = response.status_code
        film_name = response.json()
        return status_code, film_name

    @allure.step('Найти режиссера по {person_id}')
    def get_director_with_id(self, person_id: int) -> tuple:
        full_url = f"{self.url}v1.4/person/{person_id}"
        response = requests.get(full_url, headers=self.headers)
        status_code = response.status_code
        director_name = response.json()
        return status_code, director_name
