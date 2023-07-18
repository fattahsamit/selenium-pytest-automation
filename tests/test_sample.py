import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Edge()

        driver.implicitly_wait(10)
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()
        print("Test Completed!")

    def test_login(self, test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/')

        driver.find_element(By.NAME, "username").send_keys('Admin')
        driver.find_element(By.NAME, "password").send_keys('admin123')
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        x = driver.title
        assert x == 'OrangeHRM'

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed!")
