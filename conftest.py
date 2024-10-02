from selenium import webdriver
from tests.locators import LoginForm, MainWindow

import pytest
import logging
import time


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
def login(connection):
    logging.info("Вхожу в аккаунт")
    connection.get("https://stellarburgers.nomoreparties.site/")
    connection.find_element(*LoginForm.BUTTON_LOGIN).click()
    assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
        *LoginForm.HEADER_LOGIN).text == "Вход", "Неуспешный переход на страницу логина "
    connection.find_element(*LoginForm.EMAIL_INPUT).send_keys("kuznecov988@gmail.com")
    connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys("123456")
    connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
    time.sleep(2)
    assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ", ("Неуспешный вход в "
                                                                                                 "аккаунт")
