from Pages.GitAllLinks import AllLinks
from utilities.BaseClass import MainClass


class TestLinks(MainClass):
    def test_links_all(self):
        links = AllLinks(self.driver)
        links.get_all_links()
        all_links = links.get_all_links()
        assert 'https://magento.softwaretestingboard.com/#contentarea' in all_links

