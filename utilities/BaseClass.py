import pytest
import inspect
import logging

@pytest.mark.usefixtures("setup")
class MainClass:
    def get_logger(self):
        # Get the name of the test case file name at runtime
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        # Create a FileHandler instance
        file_handler = logging.FileHandler(r"C:\Users\HP\PycharmProjects\Magneto\utilities\Logfile.log")
        # Create a Formatter instance to set the log message format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(formatter)
        # Add the FileHandler to the logger
        logger.addHandler(file_handler)
        # Set the logging level to INFO
        logger.setLevel(logging.INFO)
        return logger

    def by_link_text(self, driver, locator):
        return self.driver.find_element(locator)
