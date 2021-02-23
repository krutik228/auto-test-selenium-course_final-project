from selenium.webdriver.common.by import By


""" Локаторы для поиска объектов на странице"""

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION = (By.CSS_SELECTOR, ":nth-child(1)>.alertinner strong")
    PRICE_OF_THE_PRODUCT_IN_THE_ADD_NOTIFICATION = (By.CSS_SELECTOR, ":nth-child(3)>.alertinner>p:nth-child(1) strong")
    TITTLE_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRICE_OF_THE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    NOTIFICATION_OF_ADDING_A_PRODUCT_TO_CART = (By.CSS_SELECTOR, ":nth-child(1).alert")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
