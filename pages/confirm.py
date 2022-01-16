from selenium.webdriver.common.by import By


class Confirm:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, 'country')
    purchase = (By.CSS_SELECTOR, "input.btn-success")
    country_lists = (By.XPATH, "//div[@class='suggestions']/ul/li/a")

    def get_country(self):
        return self.driver.find_element(*Confirm.country)

    def get_purchase(self):
        return self.driver.find_element(*Confirm.purchase)

    def get_list_countries(self):
        return self.driver.find_elements(*Confirm.country_lists)
