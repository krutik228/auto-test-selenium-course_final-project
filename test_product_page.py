from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8",
                                  "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.guest_can_add_product_to_basket(link)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.add_product_to_basket()
    page.guest_cant_see_success_message(link)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.guest_cant_see_success_message(link)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket(link)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, link)
    time.sleep(5)
    page.guest_cant_see_product_in_basket_opened_from_product_page(browser, link)


def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, link)
    page.guest_can_see_product_in_basket_opened_from_product_page(link)


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def register_new_user(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = f"{time.time()} + Password"
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.user_cant_see_success_message(browser, link)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.user_can_add_product_to_basket(browser, link)
