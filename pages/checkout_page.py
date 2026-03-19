from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Inputs
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")

        # Buttons
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

        # Messages
        self.success_message = (By.CLASS_NAME, "complete-header")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # Actions
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.type(self.first_name_input, first_name)
        self.type(self.last_name_input, last_name)
        self.type(self.postal_code_input, postal_code)

    def click_continue(self):
        self.click(self.continue_button)

    def click_finish(self):
        self.click(self.finish_button)

    # Success
    def get_success_message(self):
        self.wait_for_element(self.success_message)
        return self.get_text(self.success_message)

    def is_checkout_successful(self):
        return "Thank you for your order!" in self.get_success_message()

    # Error
    def get_error_message(self):
        self.wait_for_element(self.error_message)
        return self.get_text(self.error_message)

    def is_error_message_displayed(self, expected_text):
        return expected_text in self.get_error_message()