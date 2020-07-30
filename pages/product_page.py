from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_button_click(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_added_corect_book(self):
        confirm_name_book=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        confirm_name_book_basket=self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        confirm_price_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        confirm_price_book_basket = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_PRICE).text

        assert confirm_name_book in confirm_name_book_basket, f"Book {confirm_name_book} was not added to basket correctly"
        assert confirm_price_book in confirm_price_book_basket, f"Book {confirm_name_book} with price" \
                                                                f"{confirm_price_book} was not added to basket correctly"