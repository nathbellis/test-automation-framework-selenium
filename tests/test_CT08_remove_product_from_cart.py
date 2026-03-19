import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.carrinho
@pytest.mark.smoke
class TestCart:

    def test_remove_product_from_cart(self, driver):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)
        cart = CartPage(driver)

        PRODUCT = "Sauce Labs Backpack"

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        home.add_product_to_cart(PRODUCT)
        home.go_to_cart()

        # Assert
        assert cart.is_product_in_cart(PRODUCT), "Product was not added to cart"

        # Act
        cart.remove_product(PRODUCT)

        # Assert (resultado final)
        assert cart.get_cart_quantity() == 0, "Cart is not empty after removing product"
        assert not cart.is_product_in_cart(PRODUCT), "Product still present in cart after removal"