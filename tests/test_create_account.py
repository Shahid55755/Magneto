
import time

from Pages.CreateAccount import NewAccount
from utilities import testDataFile
from utilities.BaseClass import MainClass


class TestCreateUser(MainClass):
    def test_new_account(self):
        try:
            log = self.get_logger()
            new_user = NewAccount(self.driver)
            new_user.implicitly_wait()
            new = new_user.click_create_an_account()
            new.click()
            log.info("Create New account button pressed")
            new_user.enter_firstname("shahid")
            log.info("First name is shahid")
            new_user.enter_lastname("ali")
            log.info("Lastname is Ali")
            new_user.enter_email("testingz1y@test.com")
            log.info("Email is : testingz1y@yahoo.com")
            new_user.enter_password("James@12345")
            new_user.enter_confirm_password("James@12345")
            new_user.create_account().click()
            log.info("save button pressed")
            time.sleep(5)
            dup = new_user.message_register()
            print(dup.text)
            log.info(dup.text)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("create_account")
