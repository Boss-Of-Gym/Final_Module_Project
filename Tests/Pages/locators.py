from selenium.webdriver.common.by import By

class BasePageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
        LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
        LINK_BASKET_PAGE = (By.XPATH, "//span[@class='btn-group']/child::a")
        USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
        BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")

class MainPageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
        LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
        REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
        REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
        REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
        REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
        REGISTER_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
        BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/child::h1")
        PRICE_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/descendant::p[1]")
        MESSAGE_ABOUT_ADDING = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/descendant::strong[1]")
        BASKET_PRICE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/descendant::strong")
        SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")