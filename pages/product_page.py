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

        assert confirm_name_book == confirm_name_book_basket, f"Book {confirm_name_book} was not added to basket correctly,"
        assert confirm_price_book == confirm_price_book_basket, f"Book {confirm_name_book} with price" \
                                                                f"{confirm_price_book} was not added to basket correctly"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_SUCCSEFULLY_ADDED), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_SUCCSEFULLY_ADDED), \
        "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_SUCCSEFULLY_ADDED), \
            "message is disappeared but should not"