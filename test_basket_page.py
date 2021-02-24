from pages.basket_page import BasketPage


def test_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
