from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # Actions
    def open(self, url):
        self.driver.get(url)

    def login_with_credentials(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    # Validations helpers
    def is_error_message_visible(self):
        return self.is_element_visible(self.error_message)

    def get_error_message(self):
        self.wait_for_element(self.error_message)
        return self.get_text(self.error_message)

    def is_error_message_displayed(self, expected_text):
        return expected_text in self.get_error_message()