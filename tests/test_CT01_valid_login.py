import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
])
def test_valid_login_for_multiple_users(driver, username, password):

    # Arrange
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open(BASE_URL)

    # Act
    login.login_with_credentials(username, password)

    # Assert
    assert home.is_logged_in(), f"Login failed for user: {username}"