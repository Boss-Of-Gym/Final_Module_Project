import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.empty_basket
class BasketHasNoProductHere():

    @pytest.mark.xfail(reason="Заведомо падающий тест(как и должно быть)")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        print(f"Testing: {link}")
        page = ProductPage(browser, link)
        page.open()
        page.go_to_add_to_basket()
        page.should_not_be_success_message()
        print("Test passed successfully")

    @pytest.mark.xfail(reason="Ожидаемо падающий тест(кнопка не должна исчезать)")
    def test_message_disappeared_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        print(f"Testing: {link}")
        page = ProductPage(browser, link)
        page.open()
        page.go_to_add_to_basket()
        page.should_success_message_is_disappeared()
        print("Test passed successfully")

    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.basket_is_empty()
        page.text_basket_is_empty()

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        print(f"Testing: {link}")
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_and_get_code()
        print("Test passed successfully")
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        print(f"Testing: {link}")
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        print("Test passed successfully")

    