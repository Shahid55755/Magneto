
from Pages.SearchItem import SearchItem
from utilities.BaseClass import MainClass


class TestSearch(MainClass):

    def test_search(self):
        try:
            self.driver.implicitly_wait(20)
            log = self.get_logger()
            search = SearchItem(self.driver)
            first_search = search.search_item()
            log.info("Search an item")
            assert first_search.is_displayed(), "search input is not visible"
            log.info("Assert value is displayed")
            assert first_search.get_attribute("value") == "T Shirt", "Not found"
            select = search.select_item_drop_down_list()
            select.click()
            log.info("item is selected from drop down list")
            assert "Search results for" in self.driver.page_source
            element = search.pick_an_item()
            element.click()
            log.info("Item is picked")
            current = self.driver.current_url
            log.info("Verify current URL")
            assert "https://magento.softwaretestingboard.com" in current
            cart = search.add_to_cart()
            log.info("Assert Add to Cart text")
            assert "Add to Cart" in cart.text
            element = search.click_count()
            log.info("Assert Count of cart")
            assert "1" in element.text
            self.driver.quit()
        except Exception as e:
            print(f"some error occurred {str(e)}")
            self.driver.save_screenshot("search item")



