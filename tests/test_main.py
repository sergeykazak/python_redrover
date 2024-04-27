import os
import random

from dotenv import load_dotenv
import time

import allure
import pytest
from functions.functions import sort_list
from page.main_page import MainPage
from src.main_data import MainData

load_dotenv()


@allure.epic("Testing main page")
class TestMainPage:
    main_data = MainData()
    base_url = os.getenv("BASE_URL")

    def test_logout(self, driver):
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.logout()
        value = page.check_element_is_displayed()
        assert driver.current_url == self.base_url and value is True, "Login form is not seen"

    # @pytest.mark.parametrize("value", main_data.price)
    # def test_select(self, driver, value):
    #     page = MainPage(driver, self.base_url)
    #     page.open()
    #     page.login()
    #     page.logout()
    #     lst = page.check_filter(value[0])
    #     assert lst == sort_list(lst, value[1], value[2])

    def test_add_item_to_cart(self, driver):
        expectedValue = "1"
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        value = page.add_to_cart()
        assert value.text == expectedValue, f"Quantity of items is not {expectedValue}"

    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_element_is_not_presented()
        print(value)
        assert value is True, "Element is presented in DOM"

    @pytest.mark.parametrize("value", range(1, 7))
    def test(self, driver, value):
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        locator = page.check_card(value)
        print(locator)

#   instead of 'range(1, 7)' above in the decorator one can use:
# [random.choice([1, 2, 3, 4, 5, 6])]
