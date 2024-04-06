from selenium.webdriver.common.by import By
import time
from locators import Login
from data import LOGIN, PASSWORD, MAIN_PAGE

def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, Login.USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, Login.PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, Login.LOGIN_BUTTON).click()

    time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/v1/inventory.html'