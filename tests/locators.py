from selenium.webdriver.common.by import By


# Локаторы относящиеся к странице "Регистрация"
class RegistrationForm:
    LINK_REGISTRATION = (By.CLASS_NAME, "Auth_link__1fOlj")
    HEADER_REGISTRATION_PAGE = (By.XPATH, ".//main/div/h2")  # Header с названием "Регистрация"
    NAME_INPUT = (By.NAME, "name")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//fieldset[2]//input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, ".//fieldset[3]//input")  # Поле ввода пароля
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_PASSWORD_LENGTH = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")  # Сообщение об ошибке,
    # при не соблюдении длины пароля


class LoginForm:
    BUTTON_LOGIN = (By.XPATH, ".//main/section[2]/div/button")  # Кнопка "Войти в аккаунт" на главном экране
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//header/nav/a/p")  # Кнопка "Личный кабинет" на главном экране
    BUTTON_LOGIN_REGISTRATION_FORM = (By.XPATH, "//*[@id='root']//div/p/a")  # Кнопка "Войти" на экране Регистрации
    BUTTON_RESTORE_PASSWORD = (
        By.XPATH, "//*[@id='root']/div//div/p[2]/a")  # Кнопка "Восстановить пароль" на экране входа
    BUTTON_LOGIN_FORGOT_PASSWORD_FORM = (
        By.XPATH, ".//main/div/div/p/a")  # Кнопка "Войти" на экране востановления пароля
    HEADER_LOGIN = (By.XPATH, ".//main/div/h2")  # Текст "Вход" на экране Входа
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']//fieldset[1]//input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//fieldset[2]//input")  # Поле ввода password
    BUTTON_MAIN_LOGIN = (By.XPATH, "/html/body/div/div/main/div/form/button")  # Главная кнопка входа на экране Входа


class MainWindow:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//header/nav/a/p")  # Кнопка перехода в личный кабинет, с главной страницы
    BUTTON_PLACE_AN_ORDER = (
        By.XPATH, ".//main/section[2]/div/button")  # Кнопка оформить заказ, доступна после входа  в аккаунт
    BUTTON_BUILDER = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a")  # Кнопка "Конструктор"


class PersonalAccount:
    NAME = (By.XPATH, ".//main/div/div/div/ul/li[1]/div/div/input")  # Имя в главном
    BUTTON_LOG_OUT = (By.XPATH, ".//main/div/nav/ul/li[3]/button")  # Кнопка "Выйти"


class Builder:
    TAB_BREAD = (By.XPATH, ".//main/section[1]/div[1]/div[1]")  # Вкладка Булки
    TAB_BREAD_TEXT = (By.XPATH, ".//main/section[1]/div[1]/div[1]/span")
    TAB_SAUSE = (By.XPATH, ".//main/section[1]/div[1]/div[2]")  # Вкладка Соусы
    TAB_FILLING = (By.XPATH, ".//main/section[1]/div[1]/div[2]")  # Вкладка Начинки
