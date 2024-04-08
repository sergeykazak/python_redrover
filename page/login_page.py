from locators.login_locators import LoginLocators
from page.base_page import BasePage
from src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()





    def click_add_to_cart(self, locator):
        self.driver.find_element(*self.locator).click()
