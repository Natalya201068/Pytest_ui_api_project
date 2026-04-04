import allure
import pytest


@allure.title('Поиск фильма')
@allure.story('Поиск фильма по названию')
@pytest.mark.api
def test_get_film_with_query(api):
    query = 'Transformers'
    status_code, film_name = api.get_film_with_query(query)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название фильма'):
        assert film_name['docs'][0]['alternativeName'] == query


@allure.title('Поиск фильма')
@allure.story('Поиск фильма по id')
@pytest.mark.api
def test_get_film_with_id(api):
    film_id = 301
    film_query = 'The Matrix'
    status_code, film_name = api.get_film_with_id(film_id)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название фильма'):
        assert film_name['names'][1]['name'] == film_query


@allure.title('Поиск сериала')
@allure.story('Поиск сериала по id')
@pytest.mark.api
def test_get_series_with_id(api):
    series_id = 1224067
    series_query = 'Вампиры средней полосы'
    status_code, series_name = api.get_film_with_id(series_id)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название сериала'):
        assert series_name['alternativeName'] == series_query


@allure.title('Поиск персоны')
@allure.story('Поиск режиссера по id')
@pytest.mark.api
def test_get_director_with_id(api):
    director_id = 196131
    director = 'Александр Роу'
    status_code, director_name = api.get_director_with_id(director_id)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит имя режиссера'):
        assert director_name['name'] == director


@allure.title('Поиск фильма')
@allure.story('Поиск фильма с неправильным id')
@pytest.mark.api
def test_get_film_with_bad_id(api, film_id):
    film_id - 1234567890
    status_code, film_name = api.get_film_with_id(film_id)
    with allure.step('Проверить, что статус-код ответа 400'):
        assert status_code == 400
    with allure.step('Проверить, что message содержит допустимый диапазон '
                     'значений'):
        assert film_name['message'] == ['Значение поля id должно быть '
                                        'в диапазоне от 250 до 15000000!']
    with allure.step('Проверить, что error соответствует Bad Request'):
        assert film_name['error'] == 'Bad Request'
