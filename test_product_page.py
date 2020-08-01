from selenium import webdriver
from .pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage




"""
def test_add_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_button_click()




def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
"""
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(1)
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(2)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(1)
    page.basket_should_be_emty()
    page.basket_is_empty_text_is_displayed()







