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
    locked_out_user_error = browser.find_element(By.XPATH, '//h3[@data.py-test="error"][contains(text(),"Epic sadface")]')
    assert locked_out_user_error.is_displayed()
    # expected_error_message = ""
    # assert locked_out_user_error == expected_error_message, f"Expected: {expected_error_message}, Actual: {locked_out_user_error}"


def test_item_added_to_cart():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # browser.find_element(By.XPATH,'//button[contains(text(),"Open Menu")]').click()
    browser.find_element(By.XPATH,
                         '//div[text()="Sauce Labs Fleece Jacket"]/../../following-sibling::div/button').click()
    browser.find_element(By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]').click()
    item_in_cart = browser.find_element(By.XPATH, '//div[contains(text(),"Sauce Labs Fleece Jacket")]')
    time.sleep(2)
    assert item_in_cart.is_displayed()
    # browser.find_element(By.XPATH, '//[@class="btn_action checkout_button"]')
    # assert browser.current_url == 'https://www.saaaaucedemo.com/v1/inventory.html', 'Actual Result differs from Expected Result'
    # browser.quit()

def test_checkout():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # browser.find_element(By.XPATH,'//button[contains(text(),"Open Menu")]').click()
    browser.find_element(By.XPATH,
                         '//div[text()="Sauce Labs Backpack"]/../../following-sibling::div/button').click()
    cart_with_item_icon = browser.find_element(By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]')
    cart_with_item_icon.click()
    item_in_cart = browser.find_element(By.XPATH, '//div[contains(text(),"Sauce Labs Backpack")]')
    time.sleep(2)
    checkout_button = browser.find_element(By.CSS_SELECTOR, '.btn_action.checkout_button')
    checkout_button.click()
    browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys("John")
    browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Smith")
    browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("94111")
    submit_button = browser.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()
    pony_express_delivery_text = browser.find_element(By.XPATH, '//div[contains(text(), "FREE PONY EXPRESS DELIVERY!")]')
    assert pony_express_delivery_text.is_displayed()
    time.sleep(2)

    hamburger_menu = browser.find_element(By.XPATH, '//button[contains(text(), "Open Menu")]')
    hamburger_menu.click()
    time.sleep(3)
    reset_app_state_option = browser.find_element(By.CSS_SELECTOR, '#reset_sidebar_link')
    reset_app_state_option.click()
    browser.find_element(By.XPATH, '//button[contains(text(), "Close Menu")]').click()
    time.sleep(5)
    # assert cart_with_item_icon.is_displayed(), "Cart is not displayed"
    # print("Cart Text:", cart_with_item_icon.text)
    # print("Page Source:", browser.page_source)
    assert '.fa-layers-counter.shopping_cart_badge' not in browser.page_source, "Reset App State doesn't work as designed"

def test_item_info_upon_image_is_clicked():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    # browser.find_element(By.XPATH,'//button[contains(text(),"Open Menu")]').click()
    image_xpath = browser.find_element(By.XPATH, '//img[contains(@class,"inventory_item_img") and contains(@src, "sauce-backpack")]')
    image_displayed = image_xpath.is_displayed()
    assert image_displayed, "Image is not found"

    image_xpath.click()
    time.sleep(2)
    text_xpath = browser.find_element(By.XPATH, '//div[contains(text(), "carry.allTheThings() with the sleek,'
                                                ' streamlined Sly Pack")]')
    item_text_displayed = text_xpath.is_displayed()
    assert item_text_displayed, "Info about this item is not found"




