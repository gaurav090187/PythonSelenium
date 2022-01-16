import allure
import pytest

from pages.home import Home
from utilities.base_class import BaseClass
from selenium.webdriver.support.select import Select
from testdata.home_data import HomeData


class TestHomePage(BaseClass):

    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = Home(self.driver)
        log.info('Name : {}'.format(get_data['firstname']))
        home_page.get_name().send_keys(get_data['firstname'])
        home_page.get_email().send_keys(get_data['lastname'])
        self.select_option_by_text(home_page.get_gender(), get_data['gender'])
        home_page.get_check_box().click()
        home_page.get_submit().click()
        # print(driver.find_element(By.CLASS_NAME, 'alert-success').text)
        # print(driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)
        message = home_page.get_success().text
        assert 'success' in message
        self.driver.refresh()

    @pytest.fixture(params=HomeData.get_test_data('TC1'))
    def get_data(self, request):
        return request.param
