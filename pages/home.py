from selenium.webdriver.common.by import By

from pages.checkout import CheckOut


class Home:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    gender = (By.ID, 'exampleFormControlSelect1')
    check_box = (By.ID, 'exampleCheck1')
    submit = (By.XPATH, "//input[@value='Submit']")
    success = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shop_item(self):
        self.driver.find_element(*Home.shop).click()
        checkout_page = CheckOut(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*Home.name)

    def get_email(self):
        return self.driver.find_element(*Home.email)

    def get_gender(self):
        return self.driver.find_element(*Home.gender)

    def get_check_box(self):
        return self.driver.find_element(*Home.check_box)

    def get_submit(self):
        return self.driver.find_element(*Home.submit)

    def get_success(self):
        return self.driver.find_element(*Home.success)