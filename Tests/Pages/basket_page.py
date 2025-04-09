from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in text_in_basket, "Basket have any product"

    def text_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is realy empty"
