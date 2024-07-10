from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"

    def get_title(self, title, timeout=5):
        self.logger.info("Checked Title: %s" % (str(title)))
        return WebDriverWait(self.driver, timeout).until(EC.title_is(title))

    def get_element(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.driver).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

    def execute_script(self, param, timeout=3):
        pass
