from .base_page import BasePage
from .locators import  BasketPageLocators




class BasketPage(BasePage):

    def basket_should_be_emty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty but should to be'

    def basket_is_empty_text_is_displayed(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Basket is not emty' text is not shown"