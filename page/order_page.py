from locators.cart_locators import CartLocators
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
from page.base_page import BasePage


class OrderPage(BasePage):
    main_locators = MainPageLocators()
    order_locators = OrderLocators()
    cart_locators = CartLocators()


    def order_with_credentials(self, lst_data):
        self.add_item_to_cart()
        self.populate_form_fields(lst_data[0], lst_data[1], lst_data[2])
        self.click_element(self.order_locators.FINISH_BTN)
        return self.get_text(self.order_locators.SUCCESSFUL_ORDER)


    def order_without_credentials(self, lst_data):
        self.add_item_to_cart()
        self.populate_form_fields(lst_data[0], lst_data[1], lst_data[2])
        return self.get_text(self.order_locators.ERROR_MESSAGE)

        # self.click_element(self.main_locators.SAUCE_LABS_BACKPACK)
        # self.click_element(self.main_locators.CARDS_ON_PAGE)
        # self.click_element(self.cart_locators.CHECKOUT)

    def add_item_to_cart(self):
        self.element_is_clickable(self.order_locators.SAUCE_LABS_BACKPACK).click()
        self.element_is_clickable(self.order_locators.CART_ICON).click()
        self.element_is_clickable(self.cart_locators.CHECKOUT).click()


    def populate_form_fields(self, first_name, last_name, zipcode):
        self.element_is_visible(self.order_locators.FIRSTNAME).send_keys(first_name)
        self.element_is_visible(self.order_locators.LASTNAME).send_keys(last_name)
        self.element_is_visible(self.order_locators.ZIPCODE).send_keys(zipcode)
        self.element_is_clickable(self.order_locators.CONTINUE_BTN).click()

