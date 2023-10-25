from selenium.webdriver.common.by import By


class AllLinks:
    def __init__(self, driver):
        self.driver = driver

    def get_all_links(self):
        elements = self.driver.find_elements(By.TAG_NAME, "a")
        links = [element.get_attribute("href") for element in elements]
        return links

