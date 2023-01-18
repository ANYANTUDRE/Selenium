import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False, driver_path=r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        super(Booking, self).__init__(options=options)

        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

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

        search_field = self.find_element(by=By.ID, value='ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(by=By.CSS_SELECTOR,
                                                value='li[data-i="0"]'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(by=By.CSS_SELECTOR,
                                             value=f'td[data-date="{check_in_date }"]')
        check_in_element.click()

        check_out_element = self.find_element(by=By.CSS_SELECTOR,
                                              value=f'td[data-date="{check_out_date}"]')
        check_out_element.click()

        """select_numbers = self.driver.find_element(by=By.ID, value="xp__guests__toggle")
        select_numbers.click()

        increase_adult = self.driver.find_element(by=By.XPATH,
                                                  value='//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]'
                                                  )
        increase_adult.click()
        """

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID ,'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Supprimer des Adultes"]')

            decrease_adults_element.click()
            # If the value of adults reaches 1, then we should get out
            # of the while loop
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            )  # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Ajouter des Adultes"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_button.click()
