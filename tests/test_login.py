from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import LoginForm, MainWindow
from tests.constans import LINK

from data_for_tests import LoginData


class TestEntrance:

    def test_login_by_button_main_page(self, connection):
        connection.get(LINK.LINK_HOME)
        connection.find_element(*LoginForm.BUTTON_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_LOGIN))
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(LoginData.email_1)
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(LoginData.password_1)
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_by_button_personal_account(self, connection):
        connection.get(LINK.LINK_HOME)
        connection.find_element(*LoginForm.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_LOGIN))
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(LoginData.email_1)
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(LoginData.password_1)
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_from_registration_form(self, connection):
        connection.get(LINK.LINK_REGISTER)
        connection.find_element(*LoginForm.BUTTON_LOGIN_REGISTRATION_FORM).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(LoginData.email_1)
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(LoginData.password_1)
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"

    def test_login_from_remember_password_form(self, connection):
        connection.get(LINK.LINK_FORGOT_PASSWORD)
        connection.find_element(*LoginForm.BUTTON_RESTORE_PASSWORD).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_LOGIN))
        connection.find_element(*LoginForm.EMAIL_INPUT).send_keys(LoginData.email_1)
        connection.find_element(*LoginForm.PASSWORD_INPUT).send_keys(LoginData.password_1)
        connection.find_element(*LoginForm.BUTTON_MAIN_LOGIN).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).text == "Оформить заказ"
