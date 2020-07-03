import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', \
    action='store', \
    default='chrome', \
    help='Choose browser: chrome or firefox')

    parser.addoption('--language', \
    action='store', \
    default= None, \
    help='Choose language: ru, en, ... (etc.)')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', \
        {' inti. accept_languages': user_language})
        options.add_experimental_option("detach", True)
        print('\n\nStart chrome browser for test...')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\n\nStart firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> still is not implemented")
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    # time.sleep(30)
    print("\nQuit browser...")
    browser.quit()


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     options = Options()
#     options.add_experimental_option("detach", True)
#     browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe", options=options)
#     browser.maximize_window()
#     browser.implicitly_wait(10)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()