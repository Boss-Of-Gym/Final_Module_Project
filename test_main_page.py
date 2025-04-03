from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com"
    browser.get(url)
    LOGIN_LINK = browser.find_element(By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK.click()