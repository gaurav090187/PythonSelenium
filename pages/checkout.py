from selenium.webdriver.common.by import By

from pages.confirm import Confirm


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    add_checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    proceed_checkout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_products(self):
        return self.driver.find_elements(*CheckOut.products)

    def add_checkout_button(self):
        return self.driver.find_element(*CheckOut.add_checkout)

    def proceed_checkout_button(self):
        self.driver.find_element(*CheckOut.proceed_checkout).click()
        confirm_page = Confirm(self.driver)
        return confirm_page
