"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver
import time


@pytest.fixture
def browser():
    # Setup Phase
    # Initialize the EdgeDriver instance
    driver = webdriver.Edge()

    # Make its calls wait up to 10 seconds for elements to appear
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Return the WebDriver instance for the setup
    yield driver

    # Cleanup Phase

    # Delay of 2 seconds
    time.sleep(2)

    # Quit the WebDriver instance for the cleanup
    driver.close()
    driver.quit()
    print("Test Completed!")
