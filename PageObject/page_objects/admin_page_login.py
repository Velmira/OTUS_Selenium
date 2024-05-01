from selenium.webdriver.common.by import By
from OTUS_Selenium.PageObject.page_objects.base_page import BasePage


class AdminPage(BasePage):
    TITLE_MAIN = "Administration"
    TITLE_LOGGED_IN = "Dashboard"
    CARD_HEADER = By.CLASS_NAME, "card-header"
    CARD_BODY = By.CSS_SELECTOR, ".card-body"
    INPUT_USERNAME = By.XPATH, "//*[@id=\"input-username\"]"
    INPUT_PASSWORD = By.XPATH, "//*[@id=\"input-password\"]"
    LOGIN_BUTTON = By.XPATH, "//*[@id=\"form-login\"]/div[3]/button"
    LOGOUT_BUTTON = By.XPATH, "//*[@id=\"nav-logout\"]/a/span"

    FOOTER = By.ID, "footer"

    USER = "user"
    PASSWORD = "bitnami"

    def main_title(self):
        self.get_title(self.TITLE_MAIN)

    def title_logged_in(self):
        self.get_title(self.TITLE_LOGGED_IN)

    def card_header(self):
        self.get_element(self.CARD_HEADER)

    def card_body(self):
        self.get_element(self.CARD_BODY)

    def username_field(self):
        self.get_element(self.INPUT_USERNAME)

    def input_username(self):
        self.input_value(self.INPUT_USERNAME, self.USER)

    def password_field(self):
        self.get_element(self.INPUT_PASSWORD)

    def input_password(self):
        self.input_value(self.INPUT_PASSWORD, self.PASSWORD)

    def login_button(self):
        self.get_element(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    def footer(self):
        self.get_element(self.FOOTER)
