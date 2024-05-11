from selenium.webdriver.common.by import By
from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class ItemPage(BasePage):
    TITLE = "Sony VAIO"
    SEARCH_COL = By.ID, "search"
    HEADER_CART = By.ID, "header-cart"
    PRICE_NEW = By.CSS_SELECTOR, ".price-new"
    INPUT_QUANTITY = By.XPATH, "//*[@id=\"input-quantity\"]"
    ADD_TO_CART_BUTTON = By.ID, "button-cart"
    RATING_CLASS = By.CLASS_NAME, "rating"

    def main_title(self):
        self.get_title(self.TITLE)

    def search_col(self):
        self.get_element(self.SEARCH_COL)

    def header_cart(self):
        self.get_element(self.HEADER_CART)

    def price_new(self):
        self.get_element(self.PRICE_NEW)

    def input_quantity(self):
        self.get_element(self.INPUT_QUANTITY)

    def add_to_cart(self):
        self.get_element(self.ADD_TO_CART_BUTTON)

    def rating_class(self):
        self.get_element(self.RATING_CLASS)
