import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify to run on chrome/firefox")


# @pytest.fixture(scope="class", params=["chrome", "firefox"])
@pytest.fixture(scope="class", params=["chrome"])
def setup(request):
    browser_name = request.config.getoption("--browser")
    # browser_name = request.param
    if browser_name == "chrome":
        request.driver = webdriver.Chrome()
    # elif browser_name == "firefox":
    #    request.driver = webdriver.Firefox()
    request.driver.get("https://magento.softwaretestingboard.com/")
    request.driver.maximize_window()
    # else:
    #    raise ValueError(f"unsupported browser {browser_name}")
    request.cls.driver = request.driver

    yield request.driver
    request.driver.quit()
