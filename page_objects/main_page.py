import allure
import random
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    TITLE = "Your Store"
    WISHLIST_TOTAL = By.ID, "wishlist-total"
    SEARCH_COL = By.ID, "search"
    SEARCH_BUTTON = By.XPATH, "//*[@id=\"search\"]/button"
    MENU_NAVBAR = By.CSS_SELECTOR, ".container #menu"
    CAROUSEL_BANNER = By.ID, "carousel-banner-0"
    MY_ACCOUNT_BUTTON = By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/a/span"
    REGISTER_BUTTON = By.XPATH, "//*[@id=\"top\"]/div/div[2]/ul/li[2]/div/ul/li[1]/a"
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "button[title=\"Add to Cart\"]"
    DROPDOWN_CART_BUTTON = By.XPATH, "//*[@id=\"header-cart\"]/div/button"
    EURO_SIGN = By.XPATH, "//*[@href=\"EUR\"]"
    DOLLAR_SIGN = By.XPATH, "//*[@href=\"USD\"]"
    POUND_STERLING_SIGN = By.XPATH, "//*[@href=\"GBP\"]"
    SWITCH_CURRENCY_BUTTON = By.XPATH, "//*[@id =\"form-currency\"]/div"
    PRICE_NEW = By.CSS_SELECTOR, ".price-new"
    PRICE_OLD = By.CSS_SELECTOR, ".price-old"
    PRICE_TAX = By.CSS_SELECTOR, ".price-tax"

    def main_title(self):
        self.get_title(self.TITLE)

    def wishlist_total(self):
        self.get_element(self.WISHLIST_TOTAL)

    def search_col(self):
        self.get_element(self.SEARCH_COL)

    def search_button(self):
        self.get_elements(self.SEARCH_BUTTON)

    def menu_navbar(self):
        self.get_element(self.MENU_NAVBAR)

    def carousel_banner(self):
        self.get_elements(self.CAROUSEL_BANNER)

    def add_to_cart_buttons(self):
        button = self.get_elements(self.ADD_TO_CART_BUTTON)
        return button

    @allure.step("Случайный товар добавлен в корзину")
    def dropdown_cart_button(self):
        button = self.get_element(self.DROPDOWN_CART_BUTTON)
        text = button.text
        assert text.startswith("1 item(s)")
        self.logger.info("Random item is added")
        return button

    @allure.step("Выбор случайного продукта")
    def click_random_element(self, el):
        self.logger.info("Random product is chosen")
        el = self.add_to_cart_buttons()
        random_element = el[random.randint(0, 1)]
        self.execute_script("arguments[0].click();", random_element)
        return random_element

    def switch_currency_button(self):
        self.logger.info("Clicked SWITCH CURRENCY BUTTON")
        self.click(self.SWITCH_CURRENCY_BUTTON)

    @allure.step("Выбор валюты Евро")
    def euro_click(self):
        self.logger.info("Clicked EURO button")
        self.click(self.EURO_SIGN)

    @allure.step("Выбор валюты Доллар")
    def dollar_click(self):
        self.logger.info("Clicked DOLLAR button")
        self.click(self.DOLLAR_SIGN)

    @allure.step("Выбор валюты Фунты стерлингов")
    def pound_sterling_click(self):
        self.logger.info("Clicked POUND STERLING button")
        self.click(self.POUND_STERLING_SIGN)

    def prices_new(self):
        prices_new = self.get_elements(self.PRICE_NEW)
        return prices_new

    def prices_old(self):
        prices_old = self.get_elements(self.PRICE_OLD)
        return prices_old

    def prices_tax(self):
        prices_tax = self.get_elements(self.PRICE_TAX)
        return prices_tax

    def my_account_button(self):
        self.logger.info("Clicked MY ACCOUNT button")
        self.click(self.MY_ACCOUNT_BUTTON)

    def register_button(self):
        self.logger.info("Clicked Register button")
        self.click(self.REGISTER_BUTTON)

