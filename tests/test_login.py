import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import LoginForm, MainWindow


# Тут вполне можно подумать над параметризацией , сделать 1 тест, куда буду разные локаторы подкладывать
class TestEntrance:
    def setup_method(self):
        self.credentials = {
            "email": "kuznecov988@gmail.com",
            "password": "123456"
        }

    def test_login_by_button_main_page(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site/")
        connection.find_element(*LoginForm.BUTTON_LOGIN).click()
        assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(self.credentials["email"])
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(self.credentials["password"])
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_by_button_personal_account(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site/")
        connection.find_element(*LoginForm.BUTTON_PERSONAL_ACCOUNT).click()
        assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(self.credentials["email"])
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(self.credentials["password"])
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_from_registration_form(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site/register")
        connection.find_element(*LoginForm.BUTTON_LOGIN_REGISTRATION_FORM).click()
        assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(self.credentials["email"])
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(self.credentials["password"])
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_from_remember_password_form(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site/forgot-password")
        connection.find_element(*LoginForm.BUTTON_RESTORE_PASSWORD).click()
        assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(self.credentials["email"])
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(self.credentials["password"])
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"
