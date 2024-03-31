from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Chrome()

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saaaaucedemo.com/v1/inventory.html', 'Actual Result differs from Expected Result'
    browser.quit()



