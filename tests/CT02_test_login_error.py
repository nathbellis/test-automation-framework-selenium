import pytest
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.login
class TestLogin:

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "wrong_password"),
        ("invalid_user", "secret_sauce"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ])
    def test_login_error(self, driver, username, password):


        # Arrange
        login = LoginPage(driver)
        expected_error_message = "Epic sadface"

        login.open(BASE_URL)

        # Act
        login.login_with_credentials(username, password)

        # Assert
        assert login.is_error_message_visible(), f"Error message not displayed for user: {username}"
        assert login.is_error_message_displayed(expected_error_message)