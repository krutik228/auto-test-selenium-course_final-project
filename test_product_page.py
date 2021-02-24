from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8",
                                  "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()

    title_in_notification = browser.find_element(*ProductPageLocators.TITLE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
    title = browser.find_element(*ProductPageLocators.TITTLE_OF_THE_PRODUCT).text
    price_in_notification = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
    price = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text

    assert price == price_in_notification, "Цены на товар не совпадают"
    assert title == title_in_notification, "Названия товаров не совпадают"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
        "Уведомление о добавлении товара в корзину присутствует"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
        "Уведомление о добавлении товара в корзину присутствует"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    assert page.is_disappeared(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
        "Уведомление добавлении товара не исчезло"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_element_present(*ProductPageLocators.NOTIFICATION_EMPTY_BASKET), "Корзина не пустая"
    text_empty_basket = browser.find_element(*ProductPageLocators.TEXT_EMPTY_BASKET_IN_NOTIFICATION).text
    assert "Ваша корзина пуста" in text_empty_basket

def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), "Корзина пустая"


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def register_new_user(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = f"{time.time()} + Password"
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.NOTIFICATION_OF_ADDING_A_PRODUCT_TO_BASKET), \
            "Уведомление о добавлении товара в корзину присутствует"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()

        title_in_notification = browser.find_element(*ProductPageLocators.TITLE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        title = browser.find_element(*ProductPageLocators.TITTLE_OF_THE_PRODUCT).text
        price_in_notification = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION).text
        price = browser.find_element(*ProductPageLocators.PRICE_OF_THE_PRODUCT).text

        assert price == price_in_notification, "Цены на товар не совпадают"
        assert title == title_in_notification, "Названия товаров не совпадают"
