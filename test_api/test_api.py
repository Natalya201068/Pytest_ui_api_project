import allure
import pytest


@allure.title('Поиск фильма')
@allure.story('Поиск фильма по названию')
@pytest.mark.api
def test_get_film_with_query(api):
    status_code, film_name = api.get_film_with_query('Transformers')
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название фильма'):
        assert film_name['docs'][0]['alternativeName'] == 'Transformers'


@allure.title('Поиск фильма')
@allure.story('Поиск фильма по id')
@pytest.mark.api
def test_get_film_with_id(api):
    status_code, film_name = api.get_film_with_id(301)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название фильма'):
        assert film_name['names'][1]['name'] == 'The Matrix'


@allure.title('Поиск сериала')
@allure.story('Поиск сериала по id')
@pytest.mark.api
def test_get_series_with_id(api):
    status_code, series_name = api.get_film_with_id(1224067)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит название сериала'):
        assert series_name['alternativeName'] == 'Вампиры средней полосы'


@allure.title('Поиск персоны')
@allure.story('Поиск режиссера по id')
@pytest.mark.api
def test_get_director_with_id(api):
    status_code, director_name = api.get_director_with_id(196131)
    with allure.step('Проверить, что статус-код ответа 200'):
        assert status_code == 200
    with allure.step('Проверить, что тело ответа содержит имя режиссера'):
        assert director_name['name'] == 'Александр Роу'


@allure.title('Поиск фильма')
@allure.story('Поиск фильма с неправильным id')
@pytest.mark.api
def test_get_film_with_bad_id(api):
    status_code, film_name = api.get_film_with_id(1234567890)
    with allure.step('Проверить, что статус-код ответа 400'):
        assert status_code == 400
    with allure.step('Проверить, что message содержит допустимый диапазон '
                     'значений'):
        assert film_name['message'] == ['Значение поля id должно быть '
                                        'в диапазоне от 250 до 15000000!']
    with allure.step('Проверить, что error соответствует Bad Request'):
        assert film_name['error'] == 'Bad Request'
