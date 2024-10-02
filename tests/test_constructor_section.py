from locators import Builder


# При выборе той или иной вкладки меняется класс, значит выбрав вкладку и сравнив ее измененный класс можно
# определить, произошел переход на нужную вкладку или нет
class TestBuilder:

    def test_transfer_to_sauses(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site")
        connection.find_element(*Builder.TAB_SAUSE).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_SAUSE).get_attribute("class") == ("tab_tab__1SPyG "
                                                                                      "tab_tab_type_current__2BEPc "
                                                                                      "pt-4 pr-10 pb-4 pl-10 noselect")

    def test_transfer_to_bread(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site")
        connection.find_element(*Builder.TAB_SAUSE).click()
        connection.implicitly_wait(1)
        connection.find_element(*Builder.TAB_BREAD).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_BREAD).get_attribute("class") == ("tab_tab__1SPyG "
                                                                                      "tab_tab_type_current__2BEPc "
                                                                                      "pt-4 pr-10 pb-4 pl-10 noselect")

    def test_transfer_to_filling(self, connection):
        connection.get("https://stellarburgers.nomoreparties.site")
        connection.find_element(*Builder.TAB_FILLING).click()
        connection.implicitly_wait(1)
        assert connection.find_element(*Builder.TAB_FILLING).get_attribute("class") == ("tab_tab__1SPyG "
                                                                                        "tab_tab_type_current__2BEPc "
                                                                                        "pt-4 pr-10 pb-4 pl-10 noselect")
