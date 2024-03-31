import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Chrome()


def test_locked_out_user():
    browser.get('https://www.saucedemo.com/v1/')
    username = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username.send_keys("locked_out_user")
    password = browser.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("secret_sauce")
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    locked_out_user_error = browser.find_element(By.XPATH, '//h3[@data-test="error"][contains(text(),"Epic sadface")]')
    assert locked_out_user_error.is_displayed()
    # expected_error_message = ""
    # assert locked_out_user_error == expected_error_message, f"Expected: {expected_error_message}, Actual: {locked_out_user_error}"



# def test_burger_button():
#     browser.get('https://www.saucedemo.com/v1/')
#     browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     # browser.find_element(By.XPATH,'//button[contains(text(),"Open Menu")]').click()
#     browser.find_element(By.XPATH,
#                          '//div[text()="Sauce Labs Fleece Jacket"]/../../following-sibling::div/button').click()
#     browser.find_element(By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]').click()
#     browser.find_element(By.XPATH, '//[@class="btn_action checkout_button"]')
#     # assert browser.current_url == 'https://www.saaaaucedemo.com/v1/inventory.html', 'Actual Result differs from Expected Result'
#     # browser.quit()
