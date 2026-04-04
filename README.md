# Pytest_ui_api_project

## Автоматизация тестирования сайта "Кинопоиск" на Python

### _Ссылка на проект:_
[Финальный проект по ручному тестированию](https://qa116-2.yonote.ru/share/00e92b97-5ba3-43d6-a121-f494c5f006a9)
### Шаги
1. Склонировать проект 'git clone [ссылка](https://github.com/Natalya201068/Pytest_ui_api_project.git')
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'python -m pytest'
4. Запустить тесты api 'python -m pytest -m "api"'
5. Запустить тесты ui 'python -m pytest -m "ui"'
6. Сгенерировать отчет 'allure generate allure-files -o allure-report'
7. Открыть отчет 'allure open allure-report'

### Стек
- Pytest
- Selenium
- Requests
- Allure

### Структура
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- test_config.ini - настройки для тестов

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
- pip install undetected_chromedriver

### Настройка окружения

1. Создайте файл `.env` в корне проекта 
2. Заполните переменные своими данными:
 - URL=[ссылка](https://api.poiskkino.dev/)
 - X_API_KEY=your_api_key_here

  
[Ссылка на документацию](https://api.poiskkino.dev/documentation#/)


