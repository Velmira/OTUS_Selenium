from selenium.webdriver.common.by import By
from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class AdminPageProducts(BasePage):
    TITLE = "Products"
    TAB_DATA = By.XPATH, "//*[@id=\"form-product\"]/ul/li[2]/a"
    TAB_SEO = By.XPATH, "//*[@id=\"form-product\"]/ul/li[11]/a"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[@id=\"input-name-1\"]"
    CATALOG_BUTTON = By.XPATH, "//*[ @ id =\"menu-catalog\"]/a"
    PRODUCTS_BUTTON = By.XPATH, "//*[@id=\"collapse-1\"]/li[2]/a"
    ADD_BUTTON = By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a"
    META_TAG_TITLE_INPUT = By.XPATH, "//*[@id=\"input-meta-title-1\"]"
    MODEL_INPUT = By.XPATH, "//*[@id=\"input-model\"]"
    SEO_INPUT = By.XPATH, "//*[@id=\"input-keyword-0-1\"]"
    MENU_BUTTON = By.XPATH, "//*[@id=\"button-menu\"]"
    SAVE_BUTTON = By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button"
    REMOVE_BUTTON = By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button[3]"
    ALERT_ADD_PRODUCT = By.XPATH, "//*[@id=\"alert\"]"
    ALERT_SUCCESS_TEXT = "Success: You have modified products!"
    CHECKBOX_PRODUCT = By.XPATH, "//*[@id=\"form-product\"]/div[1]/table/tbody/tr[2]/td[1]/input"

    PRODUCT_NAME = "Apple Macbook Pro 16\" M2 Pro 2023"
    META_TAG_TITLE = "Apple Macbook Pro 16\" M2 Pro 2023"
    MODEL = "MNWC3"
    SEO = "macbookPro"

    def title(self):
        self.get_title(self.TITLE)

    def tab_data(self):
        self.click(self.TAB_DATA)

    def tab_seo(self):
        self.click(self.TAB_SEO)

    def product_name_input(self):
        self.input_value(self.PRODUCT_NAME_INPUT, text=AdminPageProducts.PRODUCT_NAME)

    def meta_tag_title_input(self):
        self.input_value(self.META_TAG_TITLE_INPUT, text=AdminPageProducts.META_TAG_TITLE)

    def model_input(self):
        self.input_value(self.MODEL_INPUT, text=AdminPageProducts.MODEL)

    def seo_input(self):
        self.input_value(self.SEO_INPUT, text=AdminPageProducts.SEO)

    def alert_success(self):
        alert = self.get_element(self.ALERT_ADD_PRODUCT, timeout=1)
        assert AdminPageProducts.ALERT_SUCCESS_TEXT in alert.text

    def save_button(self):
        self.click(self.SAVE_BUTTON)

    def menu_button(self):
        self.click(self.MENU_BUTTON)

    def catalog_button(self):
        self.click(self.CATALOG_BUTTON)

    def products_button(self):
        self.click(self.PRODUCTS_BUTTON)

    def add_button(self):
        self.click(self.ADD_BUTTON)

    def select_product(self):
        self.click(self.CHECKBOX_PRODUCT)

    def remove_product(self):
        self.click(self.REMOVE_BUTTON)
