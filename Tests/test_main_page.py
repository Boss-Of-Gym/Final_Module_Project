from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com"

def test_add_to_cart_button_exists(browser):
    browser.get(url)
    go_to_login_page(browser)

def go_to_login_page(browser):
    LOGIN_LINK = browser.find_element(By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK.click()