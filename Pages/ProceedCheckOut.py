import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.testDataFile import TestData
from selenium.webdriver.support.ui import Select


class Proceed:
    def __init__(self, driver):
        self.driver = driver

    def items_in_cart(self):
        wait = WebDriverWait(self.driver, 20)
        wait_item_to_view = wait.until(EC.presence_of_element_located(TestData.click_items_count))
        self.driver.execute_script("arguments[0].scrollIntoView();", wait_item_to_view)
        return wait_item_to_view

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 20)
        button = wait.until(EC.visibility_of_element_located(TestData.btn_chk_out))
        return button

    def explicit_wait(self):
        wait = WebDriverWait(self.driver, 20)
        url = wait.until(EC.url_to_be("https://magento.softwaretestingboard.com/checkout/#shipping"))
        return url

    def shipping_address(self):
        wait = WebDriverWait(self.driver, 20)
        email = wait.until(EC.visibility_of_element_located(TestData.c_email))
        email.send_keys(TestData.c_email_data)
        self.driver.find_element(*TestData.c_name).send_keys("shahid")
        self.driver.find_element(*TestData.c_l_name).send_keys("ali")
        self.driver.find_element(*TestData.c_company).send_keys("max")
        self.driver.find_element(*TestData.c_street).send_keys("address1")
        self.driver.find_element(*TestData.c_street1).send_keys("address2")
        self.driver.find_element(*TestData.c_street2).send_keys("address3")
        self.driver.find_element(*TestData.c_city).send_keys("city")
        select = Select(self.driver.find_element(*TestData.c_region))
        select.select_by_index(3)
        self.driver.find_element(*TestData.c_postcode).send_keys("12345")
        time.sleep(2)
        select = Select(self.driver.find_element(*TestData.c_country))
        select.select_by_index(3)
        self.driver.find_element(*TestData.c_telephone).send_keys("123456789")
        time.sleep(5)
        button = wait.until(EC.element_to_be_clickable(TestData.next_button))

        # Scroll the button into view
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        return button

    def place_order1(self):
        # Define the CSS selector for the "Place Order" button
        # button_selector = "button[title='Place Order']"

        # Use an explicit wait to wait for the button to be clickable
        wait = WebDriverWait(self.driver, 25)
        button = wait.until(EC.element_to_be_clickable(TestData.p_order_btn))

        # Execute the click using JavaScript
        self.driver.execute_script("arguments[0].click();", button)
        return button

    def success_message(self):
        expected_url = "https://magento.softwaretestingboard.com/checkout/onepage/success/"
        wait = WebDriverWait(self.driver, 25)
        url = wait.until(EC.url_to_be(expected_url))
        message = wait.until(EC.visibility_of_element_located(TestData.success_order))
        return message


