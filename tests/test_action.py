import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import LoginForm, MainWindow, PersonalAccount


class TestAccountAction:

    def test_transfer_to_personal_account(self, login, connection):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert connection.find_element(*PersonalAccount.NAME).get_attribute("value") == "fdsdfsfd"

    def test_transfer_from_personal_account_to_builder(self, login, connection):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        connection.find_element(*MainWindow.BUTTON_BUILDER).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_log_out_from_account(self, login, connection):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        connection.find_element(*PersonalAccount.BUTTON_LOG_OUT).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert connection.find_element(*LoginForm.HEADER_LOGIN).text == "Вход"
