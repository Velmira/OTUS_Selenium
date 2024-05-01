import datetime
import logging
import allure
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
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("opencart_tests.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    start_time = datetime.datetime.now()
    logger.info("===> Test %s started at %s" % (request.node.name, start_time))

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

    driver.log_level = log_level
    logger = logging.getLogger(request.node.name)
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    driver.maximize_window()
    driver.base_url = base_url

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    driver.close()

    end_time = datetime.datetime.now()
    logger.info("===> Test %s finished at %s \n _________ \n" % (request.node.name, end_time))
