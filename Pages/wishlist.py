import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.testDataFile import TestData
from selenium.common import StaleElementReferenceException, NoSuchElementException, WebDriverException


class MyWishList:
    def __init__(self, driver):
        self.driver = driver

    def wish_list(self):
        wait = WebDriverWait(self.driver, 20)
        add = wait.until(EC.presence_of_element_located(TestData.add_to_wishlist))
        return add
        # return self.driver.find_element(*TestData.add_to_wishlist)

    def success_wishlist(self):
        wait = WebDriverWait(self.driver, 20)
        message = wait.until(EC.presence_of_element_located(TestData.wishlist_success_msg))

    def success_msg(self):
        wait = WebDriverWait(self.driver, 20)
        msg = wait.until(EC.presence_of_element_located(TestData.message_))
        return msg

    def my_product_review(self):
        if (self.driver.find_element(*TestData.message_).text !=
                "You must login or register to add items to your wishlist."):

            wait = WebDriverWait(self.driver, 20)
            product_review = wait.until(EC.presence_of_element_located(TestData.review))
            return product_review
        else:
            print("Please register first to view product review")
