from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_button_click(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)

