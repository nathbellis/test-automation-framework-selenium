import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.checkout
@pytest.mark.smoke
class TestCheckout:

    def test_checkout_success(self, driver):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bolt T-Shirt"

        FIRST_NAME = "Nathalia"
        LAST_NAME = "Teste"
        ZIP_CODE = "12345"

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        # Act - adicionar produtos
        home.add_product_to_cart(product_1)
        home.add_product_to_cart(product_2)

        home.go_to_cart()

        # Assert - carrinho
        assert cart.is_product_in_cart(product_1), f"{product_1} not in cart"
        assert cart.is_product_in_cart(product_2), f"{product_2} not in cart"

        # Act - checkout
        cart.click_checkout()
        checkout.fill_checkout_information(FIRST_NAME, LAST_NAME, ZIP_CODE)
        checkout.click_continue()
        checkout.click_finish()

        # Assert - sucesso
        assert checkout.is_checkout_successful(), "Checkout was not completed successfully"