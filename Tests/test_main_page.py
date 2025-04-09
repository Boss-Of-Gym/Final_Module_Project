from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.basket_opened
class TestOpenedBasketFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        print(f"Testing: {link}")
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.basket_is_empty()
        page.text_basket_is_empty()
        print("Test passed successfully")

@pytest.mark.login_guest    
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.xfail(reason="Негативный тест, ожидаем что такого элемента нет на странице")
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()