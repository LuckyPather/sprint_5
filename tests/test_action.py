import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import LoginForm, MainWindow, PersonalAccount
from tests.constans import LINK
from data_for_tests import LoginData


class TestAccountAction:
    @pytest.mark.parametrize("login_data", [
    {"email": LoginData.email_1, "password": LoginData.password_1, "expected_email": LoginData.email_1},
    {"email": LoginData.email_2, "password": LoginData.password_2, "expected_email": LoginData.email_2}], indirect=["login"])
    def test_transfer_to_personal_account(self, login, connection, login_data):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_PROFILE))
        assert connection.find_element(*PersonalAccount.LOGIN_INPUT).get_attribute("value") == login_data["expected_email"]

    @pytest.mark.parametrize("login", [{"email": LoginData.email_1, "password": LoginData.password_1},
                                       {"email": LoginData.email_2, "password": LoginData.password_2}], indirect=True)
    def test_transfer_from_personal_account_to_builder(self, login, connection):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_PROFILE))
        connection.find_element(*MainWindow.BUTTON_BUILDER).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_HOME))
        assert connection.find_element(*MainWindow.BUTTON_PLACE_AN_ORDER).is_displayed() == True

    @pytest.mark.parametrize("login", [{"email": LoginData.email_1, "password": LoginData.password_1},
                                       {"email": LoginData.email_2, "password": LoginData.password_2}], indirect=True)
    def test_log_out_from_account(self, login, connection):
        connection.find_element(*MainWindow.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_PROFILE))
        connection.find_element(*PersonalAccount.BUTTON_LOG_OUT).click()
        WebDriverWait(connection, 3).until(EC.url_to_be(LINK.LINK_LOGIN))
        assert connection.find_element(*LoginForm.HEADER_LOGIN).text == "Вход"
