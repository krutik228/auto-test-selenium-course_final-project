import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_element_present(*BasketPageLocators.NOTIFICATION_EMPTY_BASKET), "Корзина не пустая"
    text_empty_basket = browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET_IN_NOTIFICATION).text
    assert "Ваша корзина пуста" in text_empty_basket


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_quest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
