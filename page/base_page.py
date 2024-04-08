from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from locators.login_locators import LoginLocators
from src.user_data import UserData


class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.element_is_visible(self.locators.USERNAME).send_keys(self.user.username)
        self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.password)
        self.element_is_clickable(self.locators.LOGIN).click()

        # Previous version when def login was on login_page:
        # self.driver.find_element(*self.locators.USERNAME).send_keys(self.user.username)
        # self.driver.find_element(*self.locators.PASSWORD).send_keys(self.user.password)
        # self.driver.find_element(*self.locators.LOGIN).click()

    def get_text(self, locator):  # метод, который возвращает text
        return self.driver.find_element(*locator).text

    def get_length(self, locator):
        return len(self.driver.find_elements(*locator))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
