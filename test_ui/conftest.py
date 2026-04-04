import allure
import pytest
from selenium import webdriver
import undetected_chromedriver as uc
import random


@pytest.fixture(scope="session")
def driver():
    with allure.step('Открыть и настроить браузер'):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        # Случайный размер окна (как у реального пользователя)
        width = random.randint(800, 1400)
        height = random.randint(600, 1000)
        chrome_options.add_argument(f'--window-size={width},{height}')
        # Язык (сайт на русском)
        chrome_options.add_argument('--lang=ru,en-US;q=0.9')
        # Реальный User-Agent
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/123.0.0.0 Safari/537.36'
        )
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
    with allure.step('Закрыть браузер'):
        driver.quit()
