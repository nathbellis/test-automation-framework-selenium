import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.sort
class TestSort:

    @pytest.mark.parametrize("sort_option, reverse", [
        ("lohi", False),  # Low → High
        ("hilo", True),   # High → Low
    ])
    def test_sort_products_by_price(self, driver, sort_option, reverse):


        # Arrange
        login = LoginPage(driver)
        home = HomePage(driver)

        login.open(BASE_URL)
        login.login_with_credentials("standard_user", "secret_sauce")

        # Act
        home.sort_products_by(sort_option)
        prices = home.get_product_prices()

        # Assert
        expected = sorted(prices, reverse=reverse)

        assert prices == expected, (
            f"Sorting failed. Actual: {prices} | Expected: {expected}"
        )