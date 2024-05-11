import random
import time

import os
import sys

sys.path.append(os.getcwd())

from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert
from OTUS_Selenium.PageObject.page_objects.main_page import MainPage
from OTUS_Selenium.PageObject.page_objects.catalog_page import CatalogPage
from OTUS_Selenium.PageObject.page_objects.item_page import ItemPage
from OTUS_Selenium.PageObject.page_objects.admin_page_login import AdminPage
from OTUS_Selenium.PageObject.page_objects.admin_page_products import AdminPageProducts
from OTUS_Selenium.PageObject.page_objects.register_page import RegisterPage




def test_main_page(browser):
    browser.get(browser.base_url)
    MainPage(browser).main_title()
    MainPage(browser).wishlist_total()
    MainPage(browser).search_col()
    MainPage(browser).search_button()
    MainPage(browser).menu_navbar()
    MainPage(browser).carousel_banner()


def test_catalog(browser):
    browser.get(browser.base_url + "catalog/laptop-notebook")
    CatalogPage(browser).main_title()
    CatalogPage(browser).compare_total()
    CatalogPage(browser).product_list()
    CatalogPage(browser).column_left()
    CatalogPage(browser).cart_button()
    CatalogPage(browser).breadcrumb()


def test_product(browser):
    browser.get(browser.base_url + "product/laptop-notebook/sony-vaio")
    ItemPage(browser).main_title()
    ItemPage(browser).search_col()
    ItemPage(browser).header_cart()
    ItemPage(browser).price_new()
    ItemPage(browser).input_quantity()
    ItemPage(browser).add_to_cart()
    ItemPage(browser).rating_class()


def test_admin(browser):
    browser.get(browser.base_url + "administration/")
    AdminPage(browser).main_title()
    AdminPage(browser).card_header()
    AdminPage(browser).card_body()
    AdminPage(browser).username_field()
    AdminPage(browser).password_field()
    AdminPage(browser).login_button()
    AdminPage(browser).footer()


def test_registration(browser):
    browser.get(browser.base_url + "index.php?route=account/register")
    RegisterPage(browser).main_title()
    RegisterPage(browser).account_set()
    RegisterPage(browser).wishlist()
    RegisterPage(browser).input_password()
    RegisterPage(browser).subscribe_news_input()
    RegisterPage(browser).continue_button()


def test_login_logout(browser):
    browser.get(browser.base_url + "administration/")
    AdminPage(browser).input_username()
    AdminPage(browser).input_password()
    AdminPage(browser).click_login_button()
    AdminPage(browser).title_logged_in()
    AdminPage(browser).click_logout_button()
    AdminPage(browser).main_title()


def test_add_random_item_from_main(browser):
    browser.get(browser.base_url)
    MainPage(browser).main_title()
    el = MainPage(browser).add_to_cart_buttons()
    random_element = el[random.randint(0, 1)]
    browser.execute_script("arguments[0].click();", random_element)
    time.sleep(1)
    text = MainPage(browser).dropdown_cart_button().text
    assert text.startswith("1 item(s)")


def test_change_currency_main(browser):
    browser.get(browser.base_url)
    MainPage(browser).main_title()
    MainPage(browser).switch_currency_button()
    MainPage(browser).euro_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "€" in prices_new.text
    for prices_old in MainPage(browser).prices_old():
        assert "€" in prices_old.text
    for prices_tax in MainPage(browser).prices_tax():
        assert "€" in prices_tax.text

    MainPage(browser).switch_currency_button()
    MainPage(browser).pound_sterling_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "£" in prices_new.text
    for prices_old in MainPage(browser).prices_old():
        assert "£" in prices_old.text
    for prices_tax in MainPage(browser).prices_tax():
        assert "£" in prices_tax.text

    MainPage(browser).switch_currency_button()
    MainPage(browser).dollar_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "$" in prices_new.text
    for prices_old in MainPage(browser).prices_old():
        assert "$" in prices_old.text
    for prices_tax in MainPage(browser).prices_tax():
        assert "$" in prices_tax.text


def test_change_currency_catalog(browser):
    browser.get(browser.base_url + "catalog/laptop-notebook")
    CatalogPage(browser).main_title()
    MainPage(browser).switch_currency_button()
    MainPage(browser).euro_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "€" in prices_new.text
    try:
        for prices_old in MainPage(browser).prices_old():
            assert "€" in prices_old.text
    except TimeoutException:
        print("Element \"prices_old\" is not on the page")
    for prices_tax in MainPage(browser).prices_tax():
        assert "€" in prices_tax.text

    MainPage(browser).switch_currency_button()
    MainPage(browser).pound_sterling_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "£" in prices_new.text
    try:
        for prices_old in MainPage(browser).prices_old():
            assert "£" in prices_old.text
    except TimeoutException:
        print("Element \"prices_old\" is not on the page")
    for prices_tax in MainPage(browser).prices_tax():
        assert "£" in prices_tax.text

    MainPage(browser).switch_currency_button()
    MainPage(browser).dollar_click()
    time.sleep(0.1)

    for prices_new in MainPage(browser).prices_new():
        assert "$" in prices_new.text
    try:
        for prices_old in MainPage(browser).prices_old():
            assert "$" in prices_old.text
    except TimeoutException:
        print("Element \"prices_old\" is not on the page")
    for prices_tax in MainPage(browser).prices_tax():
        assert "$" in prices_tax.text


def test_admin_add_new_product(browser):
    browser.get(browser.base_url + "administration/")
    AdminPage(browser).input_username()
    AdminPage(browser).input_password()
    AdminPage(browser).click_login_button()
    AdminPage(browser).title_logged_in()
    AdminPageProducts(browser).catalog_button()
    AdminPageProducts(browser).products_button()
    AdminPageProducts(browser).add_button()
    AdminPageProducts(browser).title()
    AdminPageProducts(browser).product_name_input()
    AdminPageProducts(browser).meta_tag_title_input()
    AdminPageProducts(browser).tab_data()
    AdminPageProducts(browser).model_input()
    AdminPageProducts(browser).tab_seo()
    AdminPageProducts(browser).seo_input()
    AdminPageProducts(browser).save_button()
    time.sleep(0.2)
    AdminPageProducts(browser).alert_success()


def test_admin_remove_product(browser):
    browser.get(browser.base_url + "administration/")
    AdminPage(browser).input_username()
    AdminPage(browser).input_password()
    AdminPage(browser).click_login_button()
    AdminPage(browser).title_logged_in()
    AdminPageProducts(browser).catalog_button()
    AdminPageProducts(browser).products_button()
    AdminPageProducts(browser).select_product()
    AdminPageProducts(browser).remove_product()
    Alert(browser).accept()
    time.sleep(0.1)
    AdminPageProducts(browser).alert_success()


def test_new_user_register(browser):
    browser.get(browser.base_url + "index.php?route=account/register")
    RegisterPage(browser).main_title()
    RegisterPage(browser).input_value_first_name()
    RegisterPage(browser).input_value_last_name()
    RegisterPage(browser).input_value_email()
    RegisterPage(browser).input_value_password()
    RegisterPage(browser).privacy_policy()
    RegisterPage(browser).press_continue()
    RegisterPage(browser).title_account_created()
    RegisterPage(browser).continue_to_my_account()
    RegisterPage(browser).title_my_account()
