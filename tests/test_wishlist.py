import time

import pytest
from selenium.webdriver.common.by import By

from Pages.CreateAccount import NewAccount
from Pages.ProceedCheckOut import Proceed
from Pages.SearchItem import SearchItem
from Pages.wishlist import MyWishList
from utilities.BaseClass import MainClass


class TestWishList(MainClass):

    def test_add_wish_list(self):
        try:
            log = self.get_logger()
            new_account = NewAccount(self.driver)
            log.info("Click create new account")
            new_account.click_create_an_account().click()
            log.info("First name entered")
            new_account.enter_firstname("wajid")
            log.info("Last name entered")
            new_account.enter_lastname("khan")
            log.info("Email entered")
            new_account.enter_email("waj3uuw_khan@gmail.com")
            log.info("password entered")
            new_account.enter_password("James@12345")
            log.info("Confirm password entered")
            new_account.enter_confirm_password("James@12345")
            log.info("Save/Add account")
            new_account.create_account().click()
            log.info("Implicitly wait")
            new_account.implicitly_wait()
            message = new_account.message_register()
            log.info(message.text)
            search_new_item = SearchItem(self.driver)
            log.info("Search T-Shirt")
            search_new_item.search_item()
            log.info("Select/Click in drop down list")
            search_new_item.select_item_drop_down_list().click()
            log.info("Select first shirt in class of items")
            search_new_item.pick_an_item().click()
            log.info("Selected for add to cart")
            search_new_item.add_to_cart()
            log.info("Click count of selected items")
            search_new_item.click_count()
            log.info("Object is created for wishlist page")
            obj = MyWishList(self.driver)
            log.info("Click wishlist button")
            obj.wish_list().click()
            log.info("Verify the Wish List message/Assert")
            assert_message = obj.success_msg()
            print(assert_message.text)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("Wish List")

    def test_my_product_review(self):
        try:
            obj = MyWishList(self.driver)
            my_product_review = obj.my_product_review()
            if my_product_review is not None:
                my_product_review.click()
            else:
                print("No such element found/Need to register/Login first")
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("product review")

    def test_click_reviews(self):
        try:
            log = self.get_logger()
            search_new_item = SearchItem(self.driver)
            log.info("Search T-Shirt")
            search_new_item.search_item()
            log.info("Select/Click in drop down list")
            search_new_item.select_item_drop_down_list().click()
            log.info("Select first shirt in class of items")
            search_new_item.pick_an_item()
            search_new_item.check_reviews().click()
            self.driver.implicitly_wait(10)
            txt_assert = search_new_item.assert_customer_review()
            assert txt_assert.text == "Customer Reviews"
        except Exception as e:
            print(f"An error occurred {str(e)}")
            self.driver.save_screenshot("review form")

    def test_rating(self):
        try:
            search_new_item = SearchItem(self.driver)
            assert_message = search_new_item.add_rating()
            assert "You submitted your review for moderation." in assert_message.text
            proceed = Proceed(self.driver)
            count = proceed.items_in_cart()
            count.click()
            var = proceed.proceed_to_checkout()
            var.click()
            title = proceed.explicit_wait()
            print(title)
            button = proceed.shipping_address()
            button.click()
            time.sleep(5)
            checkout = proceed.place_order1()
            assert self.driver.title == "Checkout"
            assert self.driver.current_url == "https://magento.softwaretestingboard.com/checkout/#payment"
            success = proceed.success_message()
            assert success.text == "Thank you for your purchase!"
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            self.driver.save_screenshot("rating")

