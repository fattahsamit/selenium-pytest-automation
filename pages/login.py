"""
This module contains LoginPage,
the page object for the OrangeHRM login page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    # URL
    URL = 'https://opensource-demo.orangehrmlive.com/'

    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def credentials(self, username, password):
        email_input = self.browser.find_element(*self.USERNAME_INPUT)
        email_input.send_keys(username)

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        self.browser.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
