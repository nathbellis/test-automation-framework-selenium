import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.cart
class TestCart:

    def test_add_all_products_to_cart(self, driver):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)
        cart = CartPage(driver)

        EXPECTED_PRODUCT_COUNT = 6

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        # Act
        home.add_all_products_to_cart()
        home.go_to_cart()

        # Assert
        assert cart.get_cart_quantity() == EXPECTED_PRODUCT_COUNT, (
            f"Expected {EXPECTED_PRODUCT_COUNT} products in cart"
        )