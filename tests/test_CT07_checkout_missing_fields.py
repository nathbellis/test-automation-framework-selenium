import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.checkout
@pytest.mark.smoke
class TestCheckout:

    @pytest.mark.parametrize("first_name,last_name,zip_code,expected_error", [
        ("", "Teste", "12345", "First Name is required"),
        ("Nathalia", "", "12345", "Last Name is required"),
        ("Nathalia", "Teste", "", "Postal Code is required"),
    ])
    def test_checkout_missing_fields(
        self, driver, first_name, last_name, zip_code, expected_error
    ):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        home.add_product_to_cart("Sauce Labs Backpack")
        home.go_to_cart()
        cart.click_checkout()

        # Act
        checkout.fill_checkout_information(first_name, last_name, zip_code)
        checkout.click_continue()

        # Assert
        assert checkout.is_error_message_displayed(expected_error), (
            f"Expected error '{expected_error}' not displayed"
        )