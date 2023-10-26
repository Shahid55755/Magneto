import time
from utilities.BaseClass import MainClass
from Pages.Login import LoginPage


class TestLogin(MainClass):
    def test_login_page(self):
        try:
            log = self.get_logger()
            login_pg = LoginPage(self.driver)
            login_pg.sign_in_button().click()
            log.info("signIn button pressed")
            login_pg.enter_email("abid@yahoo.com")
            login_pg.enter_password("James@122")
            login_pg.sign_in().click()
            log.info("Click sign in button after adding credentials")
            login_pg.implicitly_wait()
            user_logged = login_pg.verify_name()
            log.info(user_logged)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("login page")

    def test_invalid(self):
        try:
            log = self.get_logger()
            login_page1 = LoginPage(self.driver)
            login_page1.sign_in_button().click()
            log.info("Sign In button pressed")
            login_page1.enter_email("invalid@gmail.com")
            log.info(f"User name is {str}")
            login_page1.enter_password("123456")
            error = login_page1.sign_in_invalid()
            print(error.text)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("login error")

    def test_valid_invalid(self):
        try:
            log = self.get_logger()
            login_page1 = LoginPage(self.driver)
            login_page1.sign_in_button().click()
            log.info("Sign In button pressed")
            login_page1.enter_email("abid@yahoo.com")
            log.info(f"User name is {str}")
            login_page1.enter_password("123456")
            error = login_page1.sign_in_invalid()
            print(error.text)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("login error")

    def test_invalid_valid(self):
        try:
            log = self.get_logger()
            login_page1 = LoginPage(self.driver)
            login_page1.sign_in_button().click()
            log.info("Sign In button pressed")
            login_page1.enter_email("abid111@yahoo.com")
            log.info(f"User name is {str}")
            login_page1.enter_password("James@12")
            error = login_page1.sign_in_invalid()
            print(error.text)
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("login error")
