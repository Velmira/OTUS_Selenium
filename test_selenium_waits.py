import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.ID, "wishlist-total")))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"search\"]/button")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".container #menu")))
    wait.until(EC.visibility_of_element_located((By.ID, "carousel-banner-0")))


def test_catalog(browser):
    browser.get(browser.base_url + "catalog/laptop-notebook")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Laptops & Notebooks"))
    wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))
    wait.until(EC.visibility_of_element_located((By.ID, "product-list")))
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"header-cart\"]/div/button")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))


def test_product(browser):
    browser.get(browser.base_url + "product/laptop-notebook/macbook")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("MacBook"))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.visibility_of_element_located((By.ID, "header-cart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price-new")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"input-quantity\"]")))
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rating")))


def test_admin(browser):
    browser.get(browser.base_url + "administration/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-header")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".card-body")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"input-username\"]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"input-password\"]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"form-login\"]/div[3]/button")))
    wait.until(EC.visibility_of_element_located((By.ID, "footer")))


def test_registration(browser):
    browser.get(browser.base_url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located((By.ID, "account")))
    wait.until(EC.visibility_of_element_located((By.ID, "wishlist-total")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"input-password\"]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"input-newsletter\"]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"form-register\"]/div/button")))


def test_login_logout(browser):
    browser.get(browser.base_url + "administration/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    browser.find_element(By.XPATH, "//*[@id=\"input-username\"]").send_keys("user")
    browser.find_element(By.XPATH, "//*[@id=\"input-password\"]").send_keys("bitnami")
    browser.find_element(By.CLASS_NAME, "btn").click()
    wait.until(EC.title_is("Dashboard"))
    browser.find_element(By.XPATH, "//*[@id=\"nav-logout\"]/a/span").click()
    wait.until(EC.title_is("Administration"))


def test_add_random_item_from_main(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    el = browser.find_elements(By.CSS_SELECTOR, "button[title=\"Add to Cart\"]")
    random_element = el[random.randint(0, 1)]
    browser.execute_script("arguments[0].click();", random_element)
    time.sleep(1)
    text = browser.find_element(By.XPATH, "//*[@id=\"header-cart\"]/div/button").text
    assert text.startswith("1 item(s)")


def test_change_currency_main(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    euro = browser.find_element(By.XPATH, "//*[@href=\"EUR\"]")
    euro.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "€" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "€" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "€" in prices_tax.text
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    pound_sterling = browser.find_element(By.XPATH, "//*[@href=\"GBP\"]")
    pound_sterling.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "£" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "£" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "£" in prices_tax.text
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    usd = browser.find_element(By.XPATH, "//*[@href=\"USD\"]")
    usd.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "$" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "$" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "$" in prices_tax.text


def test_change_currency_catalog(browser):
    browser.get(browser.base_url + "catalog/laptop-notebook")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.title_is("Laptops & Notebooks"))
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    euro = browser.find_element(By.XPATH, "//*[@href=\"EUR\"]")
    euro.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "€" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "€" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "€" in prices_tax.text
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    pound_sterling = browser.find_element(By.XPATH, "//*[@href=\"GBP\"]")
    pound_sterling.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "£" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "£" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "£" in prices_tax.text
    button = browser.find_element(By.XPATH, "//*[@id =\"form-currency\"]/div")
    button.click()
    usd = browser.find_element(By.XPATH, "//*[@href=\"USD\"]")
    usd.click()
    for prices_new in browser.find_elements(By.CSS_SELECTOR, ".price-new"):
        assert "$" in prices_new.text
    for prices_old in browser.find_elements(By.CSS_SELECTOR, ".price-old"):
        assert "$" in prices_old.text
    for prices_tax in browser.find_elements(By.CSS_SELECTOR, ".price-tax"):
        assert "$" in prices_tax.text
