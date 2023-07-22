from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class FormPage:
    # URL
    URL = 'https://trytestingthis.netlify.app/'

    # Locators
    FIRSTNAME_INPUT = (By.ID, "fname")
    LASTNAME_INPUT = (By.ID, "lname")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def form_data(self, firstname, lastname):
        email_input = self.browser.find_element(*self.FIRSTNAME_INPUT)
        email_input.send_keys(firstname)

        password_input = self.browser.find_element(*self.LASTNAME_INPUT)
        password_input.send_keys(lastname)

        time.sleep(2)

        # Absolute XPATH (Not advisable for use)
        # self.browser.find_element(
        #     By.XPATH, '/html/body/div[3]/div[2]/form/fieldset/button').click()
        # Relative XPATH
        self.browser.find_element(
            By.XPATH, "//button[@class='btn btn-success']").click()
