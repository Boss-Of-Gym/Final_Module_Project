from .base_page import BasePage
from .locators import ProductPageLocators
import math, time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def add_to_basket_and_get_code(self):
        self.should_be_name_of_product()
        self.should_be_price_of_book()
        self.should_be_add_to_basket_button()
        self.go_to_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_adding()
        self.compare_basket_and_product_price()

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET), "Add to basket button not found"
    
    def should_be_name_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK), "Name of book not found"

    def should_be_price_of_book(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK), "Price of book not found"

    def should_be_message_about_adding(self):
        BOOK = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        MESSAGE = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert BOOK == MESSAGE, "Book name is not found"

    def compare_basket_and_product_price(self):
        PRICE_BOOK = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        BASKET_PRICE = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        # time.sleep(240)
        assert PRICE_BOOK == BASKET_PRICE, "Book price is not equal basket price"

    def go_to_add_to_basket(self):
        try:
            BUTTON_ADD_TO_BASKET = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
            BUTTON_ADD_TO_BASKET.click()
        except TimeoutException:
            raise AssertionError("Не удалось найти кнопку 'Add to basket' или она не кликабельна")

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        