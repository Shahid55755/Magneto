from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.testDataFile import TestData
import pytest


class NewAccount:

    def __init__(self, driver):
        self.driver = driver

    def click_create_an_account(self):
        wait = WebDriverWait(self.driver, 20)
        account = wait.until(EC.visibility_of_element_located(TestData.create_new_account))
        return account

    def enter_firstname(self, username):
        return self.driver.find_element(*TestData.firstname).send_keys(username)

    def enter_lastname(self, lastname):
        return self.driver.find_element(*TestData.lastname).send_keys(lastname)

    def enter_email(self, email):
        return self.driver.find_element(*TestData.email).send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element(*TestData.password).send_keys(password)

    def enter_confirm_password(self, confirm):
        return self.driver.find_element(*TestData.Confirm).send_keys(confirm)

    def create_account(self):
        return self.driver.find_element(*TestData.Add)

    def implicitly_wait(self):
        return self.driver.implicitly_wait(10)

    def message_register(self):
        wait = WebDriverWait(self.driver, 20)
        msg = wait.until(EC.visibility_of_element_located(TestData.duplicate_account1))
        if "There is already an account " in msg.text:
            assert "There is already an account" in msg.text
            return msg

        else:
            wait = WebDriverWait(self.driver, 20)
            msg = wait.until(EC.visibility_of_element_located(TestData.success))
            if "Thank you for registering" in msg.text:
                assert "Thank you for registering" in msg.text
                return msg

