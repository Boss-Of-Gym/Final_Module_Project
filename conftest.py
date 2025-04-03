import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= 'en', help="Choose language: en, es, fr, etc.")
    parser.addoption('--browser', action='store', default='chrome', help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")

    driver = None
    if browser_name == "chrome":
        options = OptionsChrome()
        options.add_argument(f"--lang={user_language}")
        print(f"\nStarting Chrome browser with language: {user_language}")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsFirefox()
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        options.profile = firefox_profile
        print(f"\nStarting Firefox browser with language: {user_language}")
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(f"Browser {browser_name} is not supported. Use chrome or firefox")
    
    yield driver
    print("\nClosing browser")
    driver.quit()
