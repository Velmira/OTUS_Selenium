from selenium.webdriver.common.by import By
from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    TITLE = "Register Account"
    TITLE_ACCOUNT_CREATED = "Your Account Has Been Created!"
    TITLE_MY_ACCOUNT = "My Account"

    ACCOUNT_SET = By.ID, "account"
    WISHLIST = By.ID, "wishlist-total"
    INPUT_FIRST_NAME = By.ID, "input-firstname"
    INPUT_LAST_NAME = By.ID, "input-lastname"
    INPUT_EMAIL = By.ID, "input-email"
    INPUT_PASSWORD = By.ID, "input-password"
    SUBSCRIBE_NEWS_INPUT = By.XPATH, "//*[@id=\"input-newsletter\"]"
    PRIVACY_POLICY = By.XPATH, "//*[@id=\"form-register\"]/div/div/input"
    CONTINUE_BUTTON = By.XPATH, "//*[@id=\"form-register\"]/div/button"
    CONTINUE_TO_MY_ACCOUNT_BUTTON = By.XPATH, "//*[@id =\"content\"]/div/a"

    FIRST_NAME = "IVAN"
    LAST_NAME = "IVANOV"
    EMAIL = "iivanov1999@gmail.com"
    PASSWORD = "ZXCV#$%"

    def main_title(self):
        self.get_title(self.TITLE)

    def title_account_created(self):
        self.get_title(self.TITLE_ACCOUNT_CREATED)

    def title_my_account(self):
        self.get_title(self.TITLE_MY_ACCOUNT)

    def account_set(self):
        self.get_element(self.ACCOUNT_SET)

    def wishlist(self):
        self.get_element(self.WISHLIST)

    def input_password(self):
        self.get_element(self.INPUT_PASSWORD)

    def subscribe_news_input(self):
        self.get_element(self.SUBSCRIBE_NEWS_INPUT)

    def continue_button(self):
        self.get_element(self.CONTINUE_BUTTON)

    def input_value_first_name(self):
        self.input_value(self.INPUT_FIRST_NAME, text=RegisterPage.FIRST_NAME)

    def input_value_last_name(self):
        self.input_value(self.INPUT_LAST_NAME, text=RegisterPage.LAST_NAME)

    def input_value_email(self):
        self.input_value(self.INPUT_EMAIL, text=RegisterPage.EMAIL)

    def input_value_password(self):
        self.input_value(self.INPUT_PASSWORD, text=RegisterPage.PASSWORD)

    def press_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def privacy_policy(self):
        self.click(self.PRIVACY_POLICY)

    def continue_to_my_account(self):
        self.click(self.CONTINUE_TO_MY_ACCOUNT_BUTTON)
