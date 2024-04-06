import time

USERNAME = ("css selector", "#user-name")
PASSWORD = ("css selector", "#password")
LOGIN = ("css selector", "##login-button")

def test_login(driver):
    driver.get("https://www.saucedemo.com/v1/")
    driver.find_element(*USERNAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    time.sleep(3)