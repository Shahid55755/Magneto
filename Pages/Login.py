import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.testDataFile import TestData


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def sign_in_button(self):
        return self.driver.find_element(*TestData.sign_in)

    def enter_email(self, email):
        return self.driver.find_element(*TestData.login_email).send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element(*TestData.login_password).send_keys(password)

    def sign_in(self):
        error = self.driver.find_element(*TestData.error_message)
        return error

    def sign_in_invalid(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(TestData.login_Add)).click()
        error = wait.until(EC.visibility_of_element_located(TestData.error_message))
        # error = self.driver.find_element(*TestData.error_message)
        assert "The account sign-in was incorrect or" in error.text
        return error

    def verify_name(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(TestData.verify))
        assert "Welcome, abid ali!" in element.text
        return element.text

    def implicitly_wait(self):
        return self.driver.implicitly_wait(10)
