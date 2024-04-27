import os

import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from dotenv import load_dotenv

from locators.login_locators import LoginLocators
from src.user_data import UserData

load_dotenv()


class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Open Browser")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Login")
    def login(self):
        with allure.step("Username"):
            self.element_is_visible(self.locators.USERNAME).send_keys(os.getenv("STANDARD_USER"))
        with allure.step("Password"):
            self.element_is_visible(self.locators.PASSWORD).send_keys(os.getenv("PASSWORD"))
        with allure.step("Click"):
            self.element_is_clickable(self.locators.LOGIN).click()

        # Previous version when def login was on login_page:
        # self.driver.find_element(*self.locators.USERNAME).send_keys(self.user.username)
        # self.driver.find_element(*self.locators.PASSWORD).send_keys(self.user.password)
        # self.driver.find_element(*self.locators.LOGIN).click()

    @allure.step("Get Text")
    def get_text(self, locator):  # метод, который возвращает text
        return self.driver.find_element(*locator).text

    @allure.step("Get Length")
    def get_length(self, locator):
        return len(self.driver.find_elements(*locator))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_not_presented(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_displayed(self, element):
        return element.is_displayed()

    def select_by_value(self, locator, value):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_value(value)
