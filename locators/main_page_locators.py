import random


class MainPageLocators:
    TITLE = ("css selector", ".product_label")
    CARDS = ("css selector", ".inventory_item")
    SAUCE_LABS_BACKPACK = ("css selector", "button[data-test='add-to-cart-sauce-labs-backpack']")
    REMOVE_SAUCE_LABS_BACKPACK = ("css selector", "button[id = 'remove-sauce-labs-backpack']")
    CART_BTN = ("css selector", ".shopping_cart_link")
    BURGER_MENU = ("css selector", "button[id = 'react-burger-menu-btn']")
    LOGOUT_BTN = ("css selector", "#logout_sidebar_link")
    SELECT = ("css selector", ".product_sort_container")
    PRICE_VALUE = ("css selector", ".inventory_item_price")
    COUNT_ITEMS = ("css selectors", ".shopping_cart_badge")
    CARDS_ON_PAGE = ("css selector", ".inventory_item")

    def get_card(self, value):
        return "css selector", f".inventory_item:nth-child({value})"
    #
    # CARD_LAMBDA =  lambda self, x: f".inventory_item:nth-child({x})"
    CARD_LAMBDA1 = lambda self, x: ("css selector", f".inventory_item:nth-child({x}")

    # SAUCE_LABS_BACKPACKS = [("css selector",  "button[data-test='add-to-cart-sauce-labs-backpack1']"),
    #                        ("css selector",  "button[data-test='add-to-cart-sauce-labs-backpack2']"),
    #                        ("css selector",  "button[data-test='add-to-cart-sauce-labs-backpack3']")]
    #
    # a = random.choices(SAUCE_LABS_BACKPACK, k=3)
    # print(a) #returns 3 random values from list SAUCE_LABS_BACKPACK

    # SAUCE_LABS_BACKPACK = ("xpath selector", '//div[text()="Sauce Labs Backpack"]/../../following-sibling::div/button')
    # CART_ICON = ("xpath selector", '//span[@class="fa-layers-counter shopping_cart_badge"]')

    # неправильно перечислять xpaths всех айтемов, как это сделано ниже:
    # CARD1 = ("css selector", ".inventory_item:nth-child(1)")
    # CARD2 = ("css selector", ".inventory_item:nth-child(2)")
    # CARD3 = ("css selector", ".inventory_item:nth-child(3)")
    # CARD4 = ("css selector", ".inventory_item:nth-child(4)")
    # CARD5 = ("css selector", ".inventory_item:nth-child(5)")
    # CARD6 = ("css selector", ".inventory_item:nth-child(6)")
