import allure
from selenium.webdriver.common.by import By
from OTUS_Selenium.page_objects.base_page import BasePage


class AdminPageProducts(BasePage):
    TITLE = "Products"
    CATALOG_BUTTON = By.XPATH, "//*[ @ id =\"menu-catalog\"]/a"
    PRODUCTS_BUTTON = By.XPATH, "//*[@id=\"collapse-1\"]/li[2]/a"
    ADD_BUTTON = By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a"
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

    @allure.step("Ввод названия продукта")
    def product_name_input(self):
        self.logger.info("Entered Product name: %s" % str(AdminPageProducts.PRODUCT_NAME))
        self.input_value(self.PRODUCT_NAME_INPUT, text=AdminPageProducts.PRODUCT_NAME)

    @allure.step("Ввод тайтл продукта")
    def meta_tag_title_input(self):
        self.logger.info("Entered Title: %s" % str(AdminPageProducts.META_TAG_TITLE))
        self.input_value(self.META_TAG_TITLE_INPUT, text=AdminPageProducts.META_TAG_TITLE)

    @allure.step("Ввод модели продукта")
    def model_input(self):
        self.logger.info("Entered Model: %s" % str(AdminPageProducts.MODEL))
        self.input_value(self.MODEL_INPUT, text=AdminPageProducts.MODEL)

    @allure.step("Ввод цены продукта")
    def price_input(self):
        self.logger.info("Entered Price: %s" % str(AdminPageProducts.PRICE))
        self.click(self.PRICE_INPUT)
        self.get_element(self.PRICE_INPUT).send_keys(AdminPageProducts.PRICE)

    @allure.step("Ввод SEO продукта")
    def seo_input(self):
        self.logger.info("Entered SEO: %s" % str(AdminPageProducts.SEO))
        self.input_value(self.SEO_INPUT, text=AdminPageProducts.SEO)


    @allure.step("Успешно!")
    def alert_success(self):
        alert = self.get_element(self.ALERT_ADD_PRODUCT, timeout=1)
        assert AdminPageProducts.ALERT_SUCCESS_TEXT in alert.text
        self.logger.info("Success!")

    @allure.step("Клик по кнопке Сохранить")
    def save_button(self):
        self.logger.info("Clicked save button")
        self.click(self.SAVE_BUTTON)

    def menu_button(self):
        self.logger.info("Clicked menu button")
        self.click(self.MENU_BUTTON)

    @allure.step("Выбор продукта")
    def select_product(self):
        self.logger.info("The product is chosen")
        self.click(self.CHECKBOX_PRODUCT)

    @allure.step("Клик по кнопке Удалить")
    def remove_product(self):
        self.logger.info("Clicked remove button")
        self.click(self.REMOVE_BUTTON)

    @allure.step("Переход в каталог")
    def catalog_button(self):
        self.logger.info("Clicked CATALOG Button")
        self.click(self.CATALOG_BUTTON)

    @allure.step("Переход в Продукты")
    def products_button(self):
        self.logger.info("Clicked PRODUCTS Button")
        self.click(self.PRODUCTS_BUTTON)

    @allure.step("Клик по кнопке добавления продукта")
    def add_button(self):
        self.click(self.ADD_BUTTON)
        self.logger.info("Clicked ADD NEW Button")
