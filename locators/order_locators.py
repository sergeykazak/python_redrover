
class OrderLocators:
    SAUCE_LABS_BACKPACK = ("xpath", '//div[text()="Sauce Labs Backpack"]/../../following-sibling::div/button')
    CART_ICON = ("xpath", '//span[@class="fa-layers-counter shopping_cart_badge"]')

    FIRSTNAME = ("css selector", "#first-name")
    LASTNAME = ("css selector", "#last-name")
    ZIPCODE = ("css selector", "#postal-code")
    CONTINUE_BTN = ("xpath", '//input[@type="submit"]')
    FINISH_BTN = ("xpath", '//a[@class="btn_action cart_button" ]')
    SUCCESSFUL_ORDER = ("xpath", '//h2[text()="THANK YOU FOR YOUR ORDER"]')
    ERROR_MESSAGE = ("xpath", '//h3[@data-test="error"]')
