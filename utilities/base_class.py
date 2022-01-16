import inspect
import logging

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup_teardown')
class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                                      datefmt='%d/%M/%Y %H:%M:%S')
        file_handler = logging.FileHandler('automation.log', mode='a')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def verify_elements_list_presence(self, element):
        wait = WebDriverWait(self.driver, timeout=7, poll_frequency=1)
        countries = wait.until(ec.presence_of_all_elements_located((element)))

    def select_option_by_text(self, locator, text):
        drop_down = Select(locator)
        drop_down.select_by_visible_text(text)