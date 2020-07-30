from selenium import webdriver
from .pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException


"""def inna():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    browser = webdriver.Chrome()
    browser.get(link)
    input0 = browser.find_element(By.ID, 'add_to_basket_form')
    input0.click()


    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    time.sleep(10)
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")"""


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear20199"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_button_click()

    page.solve_quiz_and_get_code()
    page.should_be_added_corect_book()

if __name__ == '__main__':
    inna()





