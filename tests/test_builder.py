from locators import Builder
from tests.constans import LINK


# При выборе той или иной вкладки меняется класс, значит выбрав вкладку и сравнив ее измененный класс можно
# определить, произошел переход на нужную вкладку или нет
class TestBuilder:

    def test_transfer_to_sauses(self, connection):
        connection.get(LINK.LINK_HOME)
        connection.find_element(*Builder.TAB_SAUCE).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_SAUCE).get_attribute("class") == Builder.SELECTED_TAB_CLASS

    def test_transfer_to_bread(self, connection):
        connection.get(LINK.LINK_HOME)
        connection.find_element(*Builder.TAB_SAUCE).click()
        connection.implicitly_wait(1)
        connection.find_element(*Builder.TAB_BREAD).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_BREAD).get_attribute("class") == Builder.SELECTED_TAB_CLASS

    def test_transfer_to_filling(self, connection):
        connection.get(LINK.LINK_HOME)
        connection.find_element(*Builder.TAB_FILLING).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_FILLING).get_attribute("class") == Builder.SELECTED_TAB_CLASS
