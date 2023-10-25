import time

import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException, WebDriverException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import MainClass
from utilities.testDataFile import TestData
from selenium.webdriver.support import expected_conditions as EC


class SearchItem:

    def __init__(self, driver):
        self.driver = driver

    def search_item(self):
        wait = WebDriverWait(self.driver, 20)
        search = wait.until(EC.visibility_of_element_located(TestData.search_id))
        search.send_keys("T Shirt")
        return search

    def select_item_drop_down_list(self):
        wait = WebDriverWait(self.driver, 20)
        select = wait.until(EC.visibility_of_element_located(TestData.select_item))
        return select

    def pick_an_item(self):
        element = self.driver.find_element(*TestData.pick_first_item)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = self.driver.find_element(*TestData.get_items)
        return element

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 20)
        """Scroll to mid of the page """
        self.driver.execute_script("window.scrollTo(0, window.scrollY + window.innerHeight / 2);")
        time.sleep(5)
        """Add to cart button"""
        add_to_cart_button = wait.until(EC.presence_of_element_located(TestData.get_add_to_path))
        """Check if Add to cart is being displayed"""
        if add_to_cart_button.is_displayed():
            """Click size button"""
            self.driver.find_element(*TestData.size).click()
            self.driver.implicitly_wait(10)
            """Click color button"""
            self.driver.find_element(*TestData.color).click()
            """Click add to cart button"""
            add_to_cart_button.click()
            """Assert to verify text"""
            element_to_assert = wait.until(EC.presence_of_element_located(TestData.cart_success_message))
            """Assert success message"""
            assert "You added" in element_to_assert.text
            return add_to_cart_button

        else:
            assert False, "Add to cart button is not visible"

    def click_count(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable(TestData.count))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def check_reviews(self):
        return self.driver.find_element(*TestData.Check_reviews)

    def assert_customer_review(self):
        c_review = self.driver.find_element(*TestData.verify_text_cus_review)
        try:
            text = self.driver.execute_script("arguments[0].scrollIntoView();", c_review)
            text = c_review
            return text
        except NoSuchElementException as e:
            print({e})

    def add_rating(self):
        try:
            button = self.driver.find_element(*TestData.rating_label)
            self.driver.implicitly_wait(10)
            ActionChains(self.driver).move_to_element(button).click(button).perform()
            self.driver.find_element(*TestData.review_form)
            self.driver.find_element(*TestData.nick_name).send_keys("Nickname")
            self.driver.find_element(*TestData.summary_field).send_keys("summary text")
            self.driver.find_element(*TestData.review_field).send_keys("review field data")
            submit_button = self.driver.find_element(*TestData.submit_button)
            submit_button.click()
            success_message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(TestData.verify_text_success)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", success_message)
            return success_message
        except Exception as e:
            pytest.fail(f"An exception occurred: {str(e)}")


