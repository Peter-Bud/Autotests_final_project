from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')

    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.ID, 'add_to_basket_form')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    BASKET_BOOK_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    BASKET_BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_SUCCSEFULLY_ADDED =(By.XPATH, '//*[@id="messages"]/div[1]/div')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')