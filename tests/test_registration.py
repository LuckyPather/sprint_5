import time

from locators import RegistrationForm, LoginForm
from tests.constans import LINK

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestRegistration:

    def test_registration_successful(self, connection, person, log_registration_success):
        connection.get(LINK.LINK_REGISTER)

        connection.find_element(*RegistrationForm.NAME_INPUT).send_keys(person.name)
        connection.find_element(*RegistrationForm.EMAIL_INPUT).send_keys(person.email)
        connection.find_element(*RegistrationForm.PASSWORD_INPUT).send_keys(person.password)

        connection.find_element(*RegistrationForm.BUTTON_REGISTRATION).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))

        assert connection.current_url == LINK.LINK_LOGIN and connection.find_element(
            *LoginForm.HEADER_LOGIN).text == "Вход"

    def test_registration_unsuccessful_invalid_password(self, connection, person, log_registration_success):
        connection.get(LINK.LINK_REGISTER)

        connection.find_element(*RegistrationForm.NAME_INPUT).send_keys(person.name)
        connection.find_element(*RegistrationForm.EMAIL_INPUT).send_keys(person.email)
        connection.find_element(*RegistrationForm.PASSWORD_INPUT).send_keys(12345)

        connection.find_element(*RegistrationForm.BUTTON_REGISTRATION).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_REGISTER))

        assert connection.current_url == LINK.LINK_REGISTER and connection.find_element(
            *RegistrationForm.ERROR_PASSWORD_LENGTH).text == "Некорректный пароль"
