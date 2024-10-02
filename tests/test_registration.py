import time
import logging

from locators import RegistrationForm, LoginForm
from utility import PersonGenerator


class TestRegistration:
    def setup_method(self, method):
        self.person = PersonGenerator()
        if method.__name__ == "test_registration_successful":
            logging.info(
                f"Запускаю тест с параметрами: Имя - {self.person.name}, Email - {self.person.email}, Пароль - {self.person.password}")
        elif method.__name__ == "test_registration_unsuccessful_invalid_password":
            logging.info(
                f"Запускаю тест с параметрами: Имя - {self.person.name}, Email - {self.person.email}, Пароль - "
                f"невалидный")

    def test_registration_successful(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site/register")

        connection.find_element(*RegistrationForm.NAME_INPUT).send_keys(self.person.name)
        connection.find_element(*RegistrationForm.EMAIL_INPUT).send_keys(self.person.email)
        connection.find_element(*RegistrationForm.PASSWORD_INPUT).send_keys(self.person.password)

        connection.find_element(*RegistrationForm.BUTTON_REGISTRATION).click()
        time.sleep(1)

        assert connection.current_url == "https://stellarburgers.nomoreparties.site/login" and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"

    def test_registration_unsuccessful_invalid_password(self,connection):
        connection.get("https://stellarburgers.nomoreparties.site/register")

        connection.find_element(*RegistrationForm.NAME_INPUT).send_keys(self.person.name)
        connection.find_element(*RegistrationForm.EMAIL_INPUT).send_keys(self.person.email)
        connection.find_element(*RegistrationForm.PASSWORD_INPUT).send_keys(12345)

        connection.find_element(*RegistrationForm.BUTTON_REGISTRATION).click()
        time.sleep(1)

        assert connection.current_url == "https://stellarburgers.nomoreparties.site/register" and connection.find_element(
            *RegistrationForm.ERROR_PASSWORD_LENGTH).text == "Некорректный пароль"
