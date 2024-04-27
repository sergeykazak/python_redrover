import random

# To add code from the missed lesson!!!!!
from locators.login_locators import LoginLocators
from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainPageLocators()
    login_locators = LoginLocators()

    def logout(self):
        self.click_element(self.main_locators.BURGER_MENU)
        self.click_element(self.main_locators.LOGOUT_BTN)

    def check_element_is_displayed(self):
        login_form = self.element_is_visible(self.login_locators.LOGIN_FORM)
        return self.element_is_displayed(login_form)

    def select(self, value):
        locator = self.main_locators.SELECT
        self.select_by_value(locator=locator, value=value)

    def get_price(self):
        lst = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        lst_price = [i.text for i in lst]
        return lst_price

    def check_filter(self, value):
        self.select(value)
        lst = self.get_price()
        return lst

    def add_to_cart(self):
        # elements = random.choices(self.main_locators.SAUCE_LABS_BACKPACKS, k = expected_value)
        self.click_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.element_is_visible(self.main_locators.COUNT_ITEMS)
        return value

    def remove_from_cart(self):
        self.click_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    def check_element_is_not_presented(self):
        return self.element_is_not_presented(self.main_locators.COUNT_ITEMS)

    # def check_card(self, value):
    #     return self.main_locators.get_card(value=value)

    # similar method as above but based on lambda:
    def check_card(self, value):
        return self.main_locators.CARD_LAMBDA1(value)
