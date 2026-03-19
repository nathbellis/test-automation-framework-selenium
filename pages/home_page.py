from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Page elements
        self.page_title = (By.CLASS_NAME, "title")
        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

        # Products
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")

        # Sort
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    # Page state
    def wait_for_home_loaded(self):
        self.wait_for_element(self.inventory_list)

    def is_logged_in(self):
        return self.is_element_visible(self.inventory_list)

    # Actions
    def add_product_to_cart(self, product_name):
        self.wait_for_home_loaded()

        add_button = (
            By.XPATH,
            f"//div[contains(@class,'inventory_item')]"
            f"[.//div[contains(text(), '{product_name}')]]//button"
        )

        self.wait_for_element(add_button)
        self.click(add_button)

    def add_all_products_to_cart(self):
        self.wait_for_home_loaded()

        buttons = self.find_elements(self.add_to_cart_buttons)

        for i in range(len(buttons)):
            self.find_elements(self.add_to_cart_buttons)[i].click()

    def go_to_cart(self):
        self.wait_for_element(self.cart_icon)
        self.click(self.cart_icon)

    # Sort
    def sort_products_by(self, value):
        self.wait_for_home_loaded()

        dropdown = Select(self.find_element(self.sort_dropdown))
        dropdown.select_by_value(value)

    # Data extraction
    def get_product_prices(self):
        self.wait_for_home_loaded()

        elements = self.find_elements(self.product_prices)
        return [float(e.text.replace("$", "")) for e in elements]