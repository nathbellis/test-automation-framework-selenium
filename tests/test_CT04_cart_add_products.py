import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.carrinho
@pytest.mark.smoke
class TestCart:

    def test_cart_add_products(self, driver):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)
        cart = CartPage(driver)

        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bolt T-Shirt"

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        # Act
        home.add_product_to_cart(product_1)
        home.go_to_cart()

        # Assert (produto 1)
        assert cart.is_product_in_cart(product_1)

        # Act (continua fluxo)
        cart.continue_shopping()
        home.wait_for_home_loaded()

        home.add_product_to_cart(product_2)
        home.go_to_cart()

        # Assert (todos)
        assert cart.is_product_in_cart(product_1)
        assert cart.is_product_in_cart(product_2)
        assert cart.get_cart_quantity() == 2