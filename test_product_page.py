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





def test_add_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_button_click()


    page.test_message_disappeared_after_adding_product_to_basket()

if __name__ == '__main__':
    inna()





