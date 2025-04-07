from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    
    def go_to_login_page(self):
        LOGIN_LINK = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        LOGIN_LINK.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not present"

    def go_to_add_to_basket(self):
        BUTTON_ADD_TO_BASKET = self.browser.find_element(*MainPageLocators.BUTTON_ADD_BASKET)
        BUTTON_ADD_TO_BASKET.click()