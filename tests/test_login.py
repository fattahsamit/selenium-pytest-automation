from pages.login import LoginPage


def test_login(browser):
    login_page = LoginPage(browser)

    # Credentials
    USERNAME = "Admin"
    PASSWORD = "admin123"

    # Given the OrangeHRM Login page is displayed
    login_page.load()

    # Check if the title matches
    x = browser.title
    assert x == 'OrangeHRM'

    # When the user enters their login credentials
    login_page.credentials(USERNAME, PASSWORD)

    # TODO: Remove this exception once the test is complete
    # raise Exception("Incomplete Test")
