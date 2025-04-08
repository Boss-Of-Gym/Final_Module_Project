import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)])    
def test_guest_can_add_product_to_basket(browser, link):
    print(f"Testing: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_and_get_code()
    print("Test passed successfully")