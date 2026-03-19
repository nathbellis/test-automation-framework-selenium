from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Locators
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")
        self.cart_list = (By.CLASS_NAME, "cart_list")

    def wait_for_cart_loaded(self):
        self.wait_for_element(self.cart_list)

    # Actions
    def click_checkout(self):
        self.wait_for_cart_loaded()
        self.click(self.checkout_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)

    def remove_product(self, product_name):
        self.wait_for_cart_loaded()

        remove_button = (
            By.XPATH,
            f"//div[@class='inventory_item_name' and text()='{product_name}']"
            f"/ancestor::div[@class='cart_item']//button"
        )

        self.click(remove_button)

    # Getters
    def get_cart_items(self):
        self.wait_for_cart_loaded()
        return [item.text for item in self.find_elements(self.cart_items)]

    def get_cart_quantity(self):
        return len(self.get_cart_items())

    def is_product_in_cart(self, product_name):
        return product_name in self.get_cart_items()