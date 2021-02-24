from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn.click()

    def guest_cant_see_success_message_after_adding_product_to_basket(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_basket()
        assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
            "Уведомление о добавлении товара в корзину присутствует"

    def guest_can_add_product_to_basket(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        title_in_notification = self.browser.find_element(
            *ProductPageLocators.TITLE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        title = self.browser.find_element(*ProductPageLocators.TITTLE_OF_THE_PRODUCT).text
        price_in_notification = self.browser.find_element(
            *ProductPageLocators.PRICE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text
        assert price == price_in_notification, "Цены на товар не совпадают"
        assert title == title_in_notification, "Названия товаров не совпадают"

    def guest_cant_see_success_message(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
            "Уведомление о добавлении товара в корзину присутствует"

    def message_disappeared_after_adding_product_to_basket(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_basket()
        assert page.is_disappeared(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
            "Уведомление добавлении товара не исчезло"

    def guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        assert page.is_element_present(*BasketPageLocators.NOTIFICATION_EMPTY_BASKET), "Корзина не пустая"
        text_empty_basket = browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET_IN_NOTIFICATION).text
        assert "Your basket is empty" in text_empty_basket

    def guest_can_see_product_in_basket_opened_from_product_page(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        page.go_to_basket()
        assert page.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), "Корзина пустая"

    def user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
            "Уведомление о добавлении товара в корзину присутствует"

    def user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

        title_in_notification = browser.find_element(*ProductPageLocators.TITLE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        title = browser.find_element(*ProductPageLocators.TITTLE_OF_THE_PRODUCT).text
        price_in_notification = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        price = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text

        assert price == price_in_notification, "Цены на товар не совпадают"
        assert title == title_in_notification, "Названия товаров не совпадают"
