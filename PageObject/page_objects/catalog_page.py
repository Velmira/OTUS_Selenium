from selenium.webdriver.common.by import By
from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class CatalogPage(BasePage):
    TITLE = "Laptops & Notebooks"
    COMPARE_TOTAL = By.ID, "compare-total"
    PRODUCT_LIST = By.ID, "product-list"
    COLUMN_LEFT = By.ID, "column-left"
    CART_BUTTON = By.XPATH, "//*[@id=\"header-cart\"]/div/button"
    BREADCRUMB = By.CLASS_NAME, "breadcrumb"

    def main_title(self):
        self.get_title(self.TITLE)

    def compare_total(self):
        self.get_element(self.COMPARE_TOTAL)

    def product_list(self):
        self.get_element(self.PRODUCT_LIST)

    def column_left(self):
        self.get_element(self.COLUMN_LEFT)

    def cart_button(self):
        self.get_element(self.CART_BUTTON)

    def breadcrumb(self):
        self.get_element(self.BREADCRUMB)
