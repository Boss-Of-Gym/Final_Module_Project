from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        LOGIN_LINK = self.browser.find_element(By.CSS_SELECTOR,'#login_link')
        LOGIN_LINK.click()
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "login link is not present"