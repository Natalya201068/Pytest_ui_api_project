from test_pages.WebPage import WebPage
import allure
import pytest
from test_ui.utils import film_names


@allure.title('Поиск фильма')
@allure.story('Поиск фильма по названию')
@pytest.mark.ui
@pytest.mark.parametrize("film_name", film_names)
def test_get_film(driver, film_name):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    film = f'{film_name}'
    web_page.get_film(film)
    with allure.step('Проверить, что название искомого фильма есть на '
                     'странице'):
        assert f'{film_name}' in driver.page_source


@allure.title('Поиск персоны')
@allure.story('Поиск актера по имени')
@pytest.mark.ui
def test_get_actor(driver):
    name_actor = 'Жан-Клод Ван Дамм'
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.get_actor(name_actor)
    with allure.step('Проверить, что актер найден'):
        assert name_actor in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск фильмов, созданных в промежуток времени')
@pytest.mark.ui
def test_search_by_years(driver):
    year1, year2 = '1935', '1944'
    film_in_years = 'Александр Невский'
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_years(year1, year2)
    with allure.step('Проверить, что в результатах поиска присутствует '
                     'фильм, созданный в выбранные годы'):
        assert film_in_years in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск информации об актере')
@pytest.mark.ui
def test_search_by_actor(driver):
    actor = 'Иннокентий Смоктуновский'
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_actor(actor)
    with allure.step('Проверить, что актер найден'):
        assert actor in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск фильма по ключевым словам')
@pytest.mark.ui
def test_search_by_keywords(driver):
    keywords = 'Инопланетная цивилизация'
    film_by_keywords = 'Отроки во Вселенной'
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_keywords(keywords)
    with allure.step('Проверить, что в результатах поиска '
                     'присутствует фильм, соответствующий запросу'):
        assert film_by_keywords in driver.page_source


@allure.title('Поиск фильма')
@allure.story('Ввод пробелов в поисковую строку')
@pytest.mark.ui
def test_search_by_space(driver):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.get_film(' ')
    with allure.step('Проверить, что по запосу ничегоне найдено'):
        assert ('К сожалению, по вашему запросу ничего '
                'не найдено...') in driver.page_source


@allure.title('Поиск фильма')
@allure.story('Нажать кнопку поиска при пустом поле ввода')
@pytest.mark.ui
def test_search_without_query(driver):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.get_film('')
    with allure.step('Проверить, что предложены условия поиска'):
        assert 'Навигатор по лучшим фильмам' in driver.page_source
