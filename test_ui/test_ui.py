from test_ui.WebPage import WebPage
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
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.get_actor('Жан-Клод Ван Дамм')
    with allure.step('Проверить, что актер найден'):
        assert 'Жан-Клод Ван Дамм' in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск фильмов, созданных в промежуток времени')
@pytest.mark.ui
def test_search_by_years(driver):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_years('1935', '1944')
    with allure.step('Проверить, что в результатах поиска присутствует '
                     'фильм, созданный в выбранные годы'):
        assert 'Александр Невский' in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск информации об актере')
@pytest.mark.ui
def test_search_by_actor(driver):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_actor('Иннокентий Смоктуновский')
    with allure.step('Проверить, что актер найден'):
        assert 'Иннокентий Смоктуновский' in driver.page_source


@allure.title('Расширенный поиск')
@allure.story('Поиск фильма по ключевым словам')
@pytest.mark.ui
def test_search_by_keywords(driver):
    web_page = WebPage(driver)
    web_page.wait_alert()
    web_page.confirm_dismiss()
    web_page.search_by_keywords('Инопланетная цивилизация')
    with allure.step('Проверить, что в результатах поиска '
                     'присутствует фильм, соответствующий запросу'):
        assert 'Отроки во Вселенной' in driver.page_source


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
