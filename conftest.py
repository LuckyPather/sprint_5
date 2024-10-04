from selenium import webdriver
from tests.locators import LoginForm, LINK

from tests.utility import PersonGenerator
import pytest
import logging



def pytest_configure(config):
    # Настраиваем логирование с уровнем INFO
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Удаляем все существующие обработчики pytest для избежания дублирования
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Устанавливаем уровень логов для CLI в pytest (выводится в реальном времени)
    config.option.log_cli = True
    config.option.log_cli_level = 'INFO'


@pytest.fixture
def connection():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(connection, request):
    email = request.param["email"]
    password = request.param["password"]

    logging.info("Вхожу в аккаунт")
    connection.get(LINK.LINK_HOME)
    connection.find_element(*LoginForm.BUTTON_LOGIN).click()
    connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(email)
    connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(password)
    connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()


@pytest.fixture
def person():
    person = PersonGenerator()
    return person


@pytest.fixture
def log_registration_success(person, request):
    # В зависимости от имени теста логируем разные данные
    if request.node.name == "test_registration_successful":
        logging.info(
            f"Запускаю тест с параметрами: Имя - {person.name}, Email - {person.email}, Пароль - {person.password}")
    elif request.node.name == "test_registration_unsuccessful_invalid_password":
        logging.info(f"Запускаю тест с параметрами: Имя - {person.name}, Email - {person.email}, Пароль - невалидный")