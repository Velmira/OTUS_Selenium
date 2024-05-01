import pytest
import webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

o = Options()
o.add_experimental_option("detach", True)

driver = webdriver_manager.chrome.ChromeDriverManager().install()
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.0.101:8880/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=o)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        service = ChromeService(executable_path=r"C:\Users\yandexdriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.base_url = base_url

    yield driver

    driver.close()
