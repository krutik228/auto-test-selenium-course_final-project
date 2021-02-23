from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

