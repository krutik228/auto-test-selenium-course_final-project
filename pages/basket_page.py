from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_link(self):
        self.quest_cant_see_product_in_the_basket(self.browser)
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/basket" in self.browser.current_url, "Неверный url-адрес"

    def quest_cant_see_product_in_the_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/basket/"
        page = BasketPage(browser, link)
        page.open()
        assert page.is_element_present(*BasketPageLocators.NOTIFICATION_EMPTY_BASKET), "Корзина не пустая"
        text_empty_basket = browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET_IN_NOTIFICATION).text
        assert "Ваша корзина пуста" in text_empty_basket
