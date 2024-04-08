import time
import pytest

from locators.main_page_locators import MainPageLocators
from page.login_page import LoginPage
from src.urls import Urls


class TestLogin:

    url = Urls()
    main_locators = MainPageLocators()

    def test_login1(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        # time.sleep(3)
        # actual_text = driver.find_element(*TITLE).text
        expected_text = "Products"
        assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"

    def test_login2(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_len = 6
        cards_on_main_page = page.get_length(self.main_locators.CARDS_ON_PAGE)
        assert cards_on_main_page == expected_len, f"Expected: {expected_len}, but actual: {cards_on_main_page}"

        # cards = driver.find_elements(*CARDS_ON_PAGE)
        # for i in cards:
        #     print(i.text)
        # print(len(cards))
        # assert len(cards) == 8, f"Expected: 6 objects on web page, actual: {len(cards)}"
        # time.sleep(3)

