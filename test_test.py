from .pages.main_page import MainPage


def test_registration(browser):
    link = "https://dev.maxbet.by/ru"
    page = MainPage(browser, link)
    page.open()
    page.close_start_windows()
    page.go_to_register_form()
    page.registration_step_1()
    page.registration_step_2()
    page.registration_step_3()
