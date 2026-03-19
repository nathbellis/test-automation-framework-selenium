import pytest
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:

    def test_locked_user_login(self, driver):


        # Arrange
        login = LoginPage(driver)
        expected_error = "Epic sadface: Sorry, this user has been locked out."

        login.open(BASE_URL)

        # Act
        login.login_with_credentials("locked_out_user", "secret_sauce")

        # Assert
        assert login.is_error_message_visible(), "Error message not displayed"
        assert login.is_error_message_displayed(expected_error)