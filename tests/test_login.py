import os

from dotenv import load_dotenv
from locators.main_page_locators import MainPageLocators
from page.login_page import LoginPage

# import collections
import allure

load_dotenv()


@allure.epic("Testing login page")
class TestLogin:

    main_locators = MainPageLocators()
    base_url = os.getenv("BASE_URL")

    @allure.title("test login1")
    @allure.description("This test check upon successful login completion user get to the main page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login1(self, driver):
        page = LoginPage(driver, self.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        # time.sleep(3)
        # actual_text = driver.find_element(*TITLE).text
        expected_text = "Products"
        assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"

    @allure.title("test login2")
    @allure.description(
        "This test check upon successful login completion user get to the main page and sees trading cards")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login2(self, driver):
        page = LoginPage(driver, self.base_url)
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
