from selenium.webdriver.common.by import By
from .base_page import BasePage


class StartPageLocators():
    CONFIRM_PUSH = (By.CSS_SELECTOR, "button#confirmWebpushButton")
    COOKIES_ACCEPT = (By.CSS_SELECTOR, "div.cookie-popup button")


class MainPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.register-buttons.register")


class RegisterPagesLocators():

    INPUT_NAME = (By.CSS_SELECTOR, "input[formcontrolname='first_name']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[formcontrolname='surname']")
    INPUT_MIDDLE_NAME = (By.CSS_SELECTOR, "input[formcontrolname='middle_name']")
    BIRTH_DAY_SELECT = (By.CSS_SELECTOR, "personal-info div.selectGroup custom-select.select:nth-child(1)")
    BIRTH_DAY_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    BIRTH_MONTH_SELECT = (By.CSS_SELECTOR, "personal-info div.selectGroup custom-select.select:nth-child(2)")
    BIRTH_MONTH_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    BIRTH_YEAR_SELECT = (By.CSS_SELECTOR, "personal-info div.selectGroup custom-select.select:nth-child(3)")
    BIRTH_YEAR_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    INPUT_MOBILE = (By.CSS_SELECTOR, "input[formcontrolname='mobile']")
    INPUT_ACCEPT_AGREEMENT = (By.XPATH, "//label/span")
    NEXT_BUTTON1 = (By.CSS_SELECTOR, "personal-info div.btns button")

    INPUT_CITY = (By.CSS_SELECTOR, "input[formcontrolname='city']")
    INPUT_ADDRESS1 = (By.CSS_SELECTOR, "input[formcontrolname='address1']")
    INPUT_USERNAME = (By.CSS_SELECTOR, "input[formcontrolname='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    INPUT_REPEATPASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='repeatPassword']")
    NEXT_BUTTON2 = (By.CSS_SELECTOR, "address-info div.btns button")

    DOCUMENT_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(1) > custom-select")
    DOCUMENT_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    DOCUMENT_NUMBER = (By.CSS_SELECTOR, "input[formcontrolname='document_number']")
    PERSONAL_ID = (By.CSS_SELECTOR, "input[formcontrolname='personal_id']")
    DOCUMENT_ISSUE_AGENCY = (By.CSS_SELECTOR, "input[formcontrolname='document_issue_agency']")
    DAY_DOC_RECEIVED_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(5) custom-select:nth-child(1)")
    DAY_DOC_RECEIVED_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    MONTH_DOC_RECEIVED_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(5) custom-select:nth-child(2)")
    MONTH_DOC_RECEIVED_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    YEAR_DOC_RECEIVED_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(5) custom-select:nth-child(3)")
    YEAR_DOC_RECEIVED_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    DAY_DOC_VALIDITY_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(6) custom-select:nth-child(1)")
    DAY_DOC_VALIDITY_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    MONTH_DOC_VALIDITY_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(6) custom-select:nth-child(2)")
    MONTH_DOC_VALIDITY_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")
    YEAR_DOC_VALIDITY_SELECT = (By.CSS_SELECTOR, "account-info div:nth-child(6) custom-select:nth-child(3)")
    YEAR_DOC_VALIDITY_OPTION = (By.CSS_SELECTOR, "div.ng-option.ng-star-inserted:nth-child(3)")