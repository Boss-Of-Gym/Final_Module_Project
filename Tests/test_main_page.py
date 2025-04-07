from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)      #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    LOGIN_PAGE = page.go_to_login_page()
    LOGIN_PAGE.should_be_login_page                         #открываем страницу


def test_should_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_should_add_book_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.go_to_add_to_basket()