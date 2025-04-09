from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login not in browser url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not here'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not here'

    def register_new_user(self, timeout = 5):
        click_login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        click_login_link.click()
        f = faker.Faker()
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(f.email())
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_password.send_keys("1234567890di")
        input_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        input_confirm_password.send_keys("1234567890di")
        click_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        click_button.click()
        print("Waiting for page to load after registration...")
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(BasePageLocators.USER_ICON))
