from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.base_class import BaseClass
from pages.home import Home
from pages.checkout import CheckOut
from pages.confirm import Confirm
import pytest
import allure


@allure.severity(allure.severity_level.MINOR)
class TestE2E(BaseClass):

    @allure.severity(allure.severity_level.MINOR)
    def test_e2e(self):
        home_page = Home(self.driver)
        checkout_page = home_page.shop_item()
        products = checkout_page.get_products()

        for product in products:
            product_name = product.find_element(By.XPATH, 'div/h4/a').text
            if product_name == 'Blackberry':
                product.find_element(By.XPATH, 'div/button').click()
                break

        checkout_page.add_checkout_button().click()
        confirm_page = checkout_page.proceed_checkout_button()
        confirm_page.get_country().send_keys('Ind')
        wait = WebDriverWait(self.driver, timeout=7, poll_frequency=1)
        countries = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
        for country in countries:
            if country.text == 'India':
                country.click()
                break

        confirm_page.get_purchase().click()
        result = wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.alert-success'), 'Thank yousda'))
        print(result)
