import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Booking:
    def __init__(self, teardown = False, driver_path=r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(15)
        # self.driver.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self, currency=None):
        self.driver.get(const.BASE_URL)

    # def change_currency(self, currency=None):
        """currency_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        selected_currency_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()"""

    def select_place_to_go(self, place_to_go):
        self.driver.get(const.BASE_URL)

        search_field = self.driver.find_element(by=By.ID, value='ss')
        search_field.clear()
        search_field.send_keys(place_to_go)


        first_result = self.driver.find_element(by=By.CSS_SELECTOR,
                                                value='li[data-i="0"]'
        )
        first_result.click()