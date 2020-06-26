from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime


link = "https://dev.maxbet.by/ru"
def test_registration():
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome("D:\Courses\drivers\chromedriver.exe", chrome_options=chrome_options)
        browser.get(link)
        browser.maximize_window()
        browser.implicitly_wait(5)

        d = datetime.datetime.now()
        d = d.strftime('%y%m%d%H%M')

        # time.sleep(5)

        confirm_push_button = browser.find_element_by_css_selector("button#confirmWebpushButton")
        confirm_push_button.click()
        cookies_accept = browser.find_element_by_css_selector("div.cookie-popup button")
        cookies_accept.click()
        registration_button = browser.find_element_by_css_selector("button.register-buttons.register")
        registration_button.click()

        input_name = browser.find_element_by_css_selector("input[formcontrolname='first_name']")
        input_name.send_keys("Иван")
        input_surname = browser.find_element_by_css_selector("input[formcontrolname='surname']")
        input_surname.send_keys("Иванов")
        input_middle_name = browser.find_element_by_css_selector("input[formcontrolname='middle_name']")
        input_middle_name.send_keys("Иванович")
        birth_day_select = browser.find_element_by_css_selector("personal-info div.selectGroup custom-select.select:nth-child(1)")
        birth_day_select.click()
        birth_day = browser.find_element_by_css_selector("div.ng-option.ng-star-inserted:nth-child(3)")
        birth_day.click()
        birth_month_select = browser.find_element_by_css_selector("personal-info div.selectGroup custom-select.select:nth-child(2)")
        birth_month_select.click()
        birth_month = browser.find_element_by_css_selector("div.ng-option.ng-star-inserted:nth-child(3)")
        birth_month.click()
        birth_year_select = browser.find_element_by_css_selector("personal-info div.selectGroup custom-select.select:nth-child(3)")
        birth_year_select.click()
        birth_year = browser.find_element_by_css_selector("div.ng-option.ng-star-inserted:nth-child(3)")
        birth_year.click()
        input_email = browser.find_element_by_css_selector("input[formcontrolname='email']")
        input_email.send_keys("2kn15b.dobera@gmail.com")
        input_mobile = browser.find_element_by_css_selector("input[formcontrolname='mobile']")
        input_mobile.send_keys("1234567")
        input_accept_agreement = browser.find_element_by_xpath("//label/span")
        browser.execute_script("return arguments[0].scrollIntoView(true);", input_accept_agreement)
        input_accept_agreement.click()
        next_button1 = browser.find_element_by_css_selector("personal-info div.btns button")
        next_button1.click()

        input_city = browser.find_element_by_css_selector("input[formcontrolname='city']")
        input_city.send_keys("Бучми")
        input_address1 = browser.find_element_by_css_selector("input[formcontrolname='address1']")
        input_address1.send_keys("вул. Пушкина 228")
        input_username = browser.find_element_by_css_selector("input[formcontrolname='username']")
        input_username.send_keys(f"test{d}")
        input_password = browser.find_element_by_css_selector("input[formcontrolname='password']")
        input_password.send_keys("qwerty123")
        input_repeatPassword = browser.find_element_by_css_selector("input[formcontrolname='repeatPassword']")
        input_repeatPassword.send_keys("qwerty123")
        next_button2 = browser.find_element_by_css_selector("address-info div.btns button")
        next_button2.click()

        document_select = browser.find_element_by_css_selector("account-info div:nth-child(1) > custom-select")
        document_select.click()
        document = browser.find_element_by_css_selector("div.ng-option.ng-star-inserted:nth-child(3)")
        document.click()
        document_number = browser.find_element_by_css_selector("input[formcontrolname='document_number']")
        document_number.send_keys("ds1234567")
        personal_id = browser.find_element_by_css_selector("input[formcontrolname='personal_id']")
        personal_id.send_keys("12345678901234")
    finally:
        time.sleep(3)
        # browser.quit()