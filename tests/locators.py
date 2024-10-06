from selenium.webdriver.common.by import By


# Локаторы относящиеся к странице "Регистрация"
class RegistrationForm:
    NAME_INPUT = (By.NAME, "name")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле ввода пароля
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_PASSWORD_LENGTH = (
    By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке при не соблюдении длины пароля


class LoginForm:
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главном экране
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный кабинет" на главном экране
    BUTTON_LOGIN_REGISTRATION_FORM = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" на экране Регистрации
    BUTTON_RESTORE_PASSWORD = (
        By.XPATH, ".//a[text()='Восстановить пароль'")  # Кнопка "Восстановить пароль" на экране входа
    BUTTON_LOGIN_FORGOT_PASSWORD_FORM = (
        By.XPATH, ".//a[text()='Войти'")  # Кнопка "Войти" на экране востановления пароля
    HEADER_LOGIN = (By.XPATH, ".//h2[text()='Вход'")  # Текст "Вход" на экране Входа
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле ввода password
    BUTTON_MAIN_LOGIN = (By.XPATH, ".//button[text() = 'Войти']")  # Главная кнопка входа на экране Входа


class MainWindow:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".p[text() = 'Личный кабинет']")  # Кнопка перехода в личный кабинет, с главной страницы
    BUTTON_PLACE_AN_ORDER = (
        By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка оформить заказ, доступна после входа  в аккаунт
    BUTTON_BUILDER = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"


class PersonalAccount:
    LOGIN_INPUT = (By.XPATH, ".//label[text()='Логин']/following-sibling::input")
    BUTTON_LOG_OUT = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выйти"


class Builder:
    TAB_BREAD = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Булки']")  # Вкладка Булки
    TAB_SAUCE = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']")  # Вкладка Соусы
    TAB_FILLING = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']")  # Вкладка Начинки
    SELECTED_TAB_CLASS = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"  # Класс для выбраной вкладки
