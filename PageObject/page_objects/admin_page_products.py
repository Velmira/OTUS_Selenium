import allure
from selenium.webdriver.common.by import By

from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class AdminPageProducts(BasePage):
    TITLE = "Products"
    TAB_DATA = By.XPATH, "//*[@id=\"form-product\"]/ul/li[2]/a"
    TAB_SEO = By.XPATH, "//*[@id=\"form-product\"]/ul/li[11]/a"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[@id=\"input-name-1\"]"
    META_TAG_TITLE_INPUT = By.XPATH, "//*[@id=\"input-meta-title-1\"]"
    MODEL_INPUT = By.XPATH, "//*[@id=\"input-model\"]"
    PRICE_INPUT = By.XPATH, "//*[@id=\"input-price\"]"
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
    PRICE = "2550"
    SEO = "macbookPro"

    def title(self):
        self.get_title(self.TITLE)

    def tab_data(self):
        self.click(self.TAB_DATA)

    def tab_seo(self):
        self.click(self.TAB_SEO)

    @allure.step("���� �������� ��������")
    def product_name_input(self):
        self.logger.info("Entered Product name: %s" % str(AdminPageProducts.PRODUCT_NAME))
        self.input_value(self.PRODUCT_NAME_INPUT, text=AdminPageProducts.PRODUCT_NAME)

    @allure.step("���� ����� ��������")
    def meta_tag_title_input(self):
        self.logger.info("Entered Title: %s" % str(AdminPageProducts.META_TAG_TITLE))
        self.input_value(self.META_TAG_TITLE_INPUT, text=AdminPageProducts.META_TAG_TITLE)

    @allure.step("���� ������ ��������")
    def model_input(self):
        self.logger.info("Entered Model: %s" % str(AdminPageProducts.MODEL))
        self.input_value(self.MODEL_INPUT, text=AdminPageProducts.MODEL)

    @allure.step("���� ���� ��������")
    def price_input(self):
        self.logger.info("Entered Price: %s" % str(AdminPageProducts.PRICE))
        self.click(self.PRICE_INPUT)
        self.get_element(self.PRICE_INPUT).send_keys(AdminPageProducts.PRICE)

    @allure.step("���� SEO ��������")
    def seo_input(self):
        self.logger.info("Entered SEO: %s" % str(AdminPageProducts.SEO))
        self.input_value(self.SEO_INPUT, text=AdminPageProducts.SEO)


    @allure.step("�������!")
    def alert_success(self):
        alert = self.get_element(self.ALERT_ADD_PRODUCT, timeout=1)
        assert AdminPageProducts.ALERT_SUCCESS_TEXT in alert.text
        self.logger.info("Success!")

    @allure.step("���� �� ������ ���������")
    def save_button(self):
        self.logger.info("Clicked save button")
        self.click(self.SAVE_BUTTON)

    def menu_button(self):
        self.logger.info("Clicked menu button")
        self.click(self.MENU_BUTTON)

    @allure.step("����� ��������")
    def select_product(self):
        self.logger.info("The product is chosen")
        self.click(self.CHECKBOX_PRODUCT)

    @allure.step("���� �� ������ �������")
    def remove_product(self):
        self.logger.info("Clicked remove button")
        self.click(self.REMOVE_BUTTON)
