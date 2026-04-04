import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WebPage:

    def __init__(self, driver: WebDriver) -> None:
        self.ui_url = 'https://www.kinopoisk.ru'
        self.driver = driver

    @allure.step('Пройти captcha')
    def wait_alert(self) -> None:
        self.driver.get(self.ui_url)
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.ID, 'js-button'))
            ).click()
        except Exception:
            pass

    @allure.step('Закрыть рекламный баннер, если есть')
    def confirm_dismiss(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((
                    By.XPATH, '//button[text()="Не сейчас"]'))
            ).click()
        except Exception:
            pass

    @allure.step('Найти фильм по названию. Ввод в поисковой строке.')
    def get_film(self, film_name: str) -> None:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'input[name="kp_query"]'))
        ).send_keys(film_name)
        button = self.driver.find_element(By.CLASS_NAME,
                                          'search-form-submit-button__icon')
        button.click()

    @allure.step('Найти актера по имени. Ввод в поисковой строке.')
    def get_actor(self, actor_name: str) -> None:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'input[name="kp_query"]'))
        ).send_keys(actor_name)
        button = self.driver.find_element(
            By.CLASS_NAME, 'search-form-submit-button__icon')
        button.click()

    @allure.step('Найти фильм по годам создания. Расширенный поиск.')
    def search_by_years(self, year1: str, year2: str) -> None:
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'a[aria-label="Расширенный поиск"]'))
        )
        element.click()
        field1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              'select#from_year'))
        )
        field1.send_keys(year1)
        field2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'select#to_year'))
        )
        field2.send_keys(year2)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input.el_18.submit.nice_button'))
        )
        button.click()

    @allure.step('Найти актера по имени. Расширенный поиск.')
    def search_by_actor(self, actor) -> None:
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'a[aria-label="Расширенный поиск"]'))
        )
        element.click()
        element_actor = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'find_people'))
        )
        element_actor.send_keys(actor)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'input.el_8.submit.nice_button'))
        )
        button.click()

    @allure.step('Найти фильм по ключевым словам. Расширенный поиск.')
    def search_by_keywords(self, keywords) -> None:
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'a[aria-label="Расширенный поиск"]'))
        )
        element.click()
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'find_keyword'))
        )
        element.send_keys(keywords)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'form#keyword_search > input.submit.nice_button'))
        )
        button.click()
