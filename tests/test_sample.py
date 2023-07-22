from pages.form import FormPage


def test_sample(browser):
    login_page = FormPage(browser)

    FIRSTNAME_INPUT = "Admin"
    LASTNAME_INPUT = "admin123"

    login_page.load()
    login_page.form_data(FIRSTNAME_INPUT, LASTNAME_INPUT)
