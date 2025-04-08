from selenium.webdriver.common.by import By

class MainPageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
        LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
        REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
        BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/child::h1")
        PRICE_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/descendant::p[1]")
        MESSAGE_ABOUT_ADDING = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/descendant::strong[1]")
        BASKET_PRICE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/descendant::strong")