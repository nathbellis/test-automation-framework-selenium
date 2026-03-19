from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text, clear_first=True):
        element = self.find_element(locator)

        if clear_first:
            element.clear()

        element.send_keys(text)

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def is_element_visible(self, locator):
        elements = self.find_elements(locator)
        return len(elements) > 0 and elements[0].is_displayed()

    def assert_element_visible(self, locator):
        assert self.is_element_visible(locator), f"Element '{locator}' is not visible on the page."

    def assert_element_not_present(self, locator):
        assert len(self.find_elements(locator)) == 0, f"Element '{locator}' is present but should not be."

    def wait_for_text(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )