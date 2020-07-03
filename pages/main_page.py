from .locators import MainPageLocators
from .locators import StartPageLocators
from .locators import RegisterPagesLocators
from .generators import *
from .base_page import BasePage


class MainPage(BasePage):

    def close_start_windows(self):
        confirm_push = self.browser.find_element(*StartPageLocators.CONFIRM_PUSH)
        confirm_push.click()
        cookies_accept = self.browser.find_element(*StartPageLocators.COOKIES_ACCEPT)
        cookies_accept.click()

    def go_to_register_form(self):
        register_button = self.browser.find_element(*MainPageLocators.REGISTER_BUTTON)
        register_button.click()

    def registration_step_1(self):
        name = self.browser.find_element(*RegisterPagesLocators.INPUT_NAME)
        name.send_keys(randomStringCirillic())
        surname = self.browser.find_element(*RegisterPagesLocators.INPUT_SURNAME)
        surname.send_keys(randomStringCirillic())
        middle_name = self.browser.find_element(*RegisterPagesLocators.INPUT_MIDDLE_NAME)
        middle_name.send_keys(randomStringCirillic())
        birth_day_select = self.browser.find_element(*RegisterPagesLocators.BIRTH_DAY_SELECT)
        birth_day_select.click()
        birth_day_option = self.browser.find_element(*RegisterPagesLocators.BIRTH_DAY_OPTION)
        birth_day_option.click()
        birth_month_select = self.browser.find_element(*RegisterPagesLocators.BIRTH_MONTH_SELECT)
        birth_month_select.click()
        birth_month_option = self.browser.find_element(*RegisterPagesLocators.BIRTH_MONTH_OPTION)
        birth_month_option.click()
        birth_year_select = self.browser.find_element(*RegisterPagesLocators.BIRTH_YEAR_SELECT)
        birth_year_select.click()
        birth_year_option = self.browser.find_element(*RegisterPagesLocators.BIRTH_YEAR_OPTION)
        birth_year_option.click()
        email = self.browser.find_element(*RegisterPagesLocators.INPUT_EMAIL)
        email.send_keys("2kn15b.dobera@gmail.com")
        mobile = self.browser.find_element(*RegisterPagesLocators.INPUT_MOBILE)
        mobile.send_keys(randomDigits(7))
        accept_argeement = self.browser.find_element(*RegisterPagesLocators.INPUT_ACCEPT_AGREEMENT)
        accept_argeement.click()
        next1 = self.browser.find_element(*RegisterPagesLocators.NEXT_BUTTON1)
        next1.click()
        assert True

    def registration_step_2(self):
        city = self.browser.find_element(*RegisterPagesLocators.INPUT_CITY)
        city.send_keys(randomStringCirillic())
        address = self.browser.find_element(*RegisterPagesLocators.INPUT_ADDRESS1)
        address.send_keys(randomStringCirillic())
        username = self.browser.find_element(*RegisterPagesLocators.INPUT_USERNAME)
        username.send_keys(f"test{generate_username()}")
        password = self.browser.find_element(*RegisterPagesLocators.INPUT_PASSWORD)
        password.send_keys("qwerty123")
        repeat_password = self.browser.find_element(*RegisterPagesLocators.INPUT_REPEATPASSWORD)
        repeat_password.send_keys("qwerty123")
        next2 = self.browser.find_element(*RegisterPagesLocators.NEXT_BUTTON2)
        next2.click()
        assert True

    def registration_step_3(self):
        document_select = self.browser.find_element(*RegisterPagesLocators.DOCUMENT_SELECT)
        document_select.click()
        document_option = self.browser.find_element(*RegisterPagesLocators.DOCUMENT_OPTION)
        document_option.click()
        document_number = self.browser.find_element(*RegisterPagesLocators.DOCUMENT_NUMBER)
        document_number.send_keys(randomDigits(9))
        personal_id = self.browser.find_element(*RegisterPagesLocators.PERSONAL_ID)
        personal_id.send_keys(generate_id())
        document_issue_agency = self.browser.find_element(*RegisterPagesLocators.DOCUMENT_ISSUE_AGENCY)
        document_issue_agency.send_keys(randomStringCirillic())
        day_doc_received = self.browser.find_element(*RegisterPagesLocators.DAY_DOC_RECEIVED_SELECT)
        day_doc_received.click()
        day_doc_received_option = self.browser.find_element(*RegisterPagesLocators.DAY_DOC_RECEIVED_OPTION)
        day_doc_received_option.click()
        month_doc_received = self.browser.find_element(*RegisterPagesLocators.MONTH_DOC_RECEIVED_SELECT)
        month_doc_received.click()
        month_doc_received_option = self.browser.find_element(*RegisterPagesLocators.MONTH_DOC_RECEIVED_OPTION)
        month_doc_received_option.click()
        year_doc_received = self.browser.find_element(*RegisterPagesLocators.YEAR_DOC_RECEIVED_SELECT)
        year_doc_received.click()
        year_doc_received_option = self.browser.find_element(*RegisterPagesLocators.YEAR_DOC_RECEIVED_OPTION)
        year_doc_received_option.click()
        day_doc_validity = self.browser.find_element(*RegisterPagesLocators.DAY_DOC_VALIDITY_SELECT)
        day_doc_validity.click()
        day_doc_validity_option = self.browser.find_element(*RegisterPagesLocators.DAY_DOC_VALIDITY_OPTION)
        day_doc_validity_option.click()
        month_doc_validity = self.browser.find_element(*RegisterPagesLocators.MONTH_DOC_VALIDITY_SELECT)
        month_doc_validity.click()
        month_doc_validity_option = self.browser.find_element(*RegisterPagesLocators.MONTH_DOC_VALIDITY_OPTION)
        month_doc_validity_option.click()
        year_doc_validity = self.browser.find_element(*RegisterPagesLocators.YEAR_DOC_VALIDITY_SELECT)
        year_doc_validity.click()
        year_doc_validity_option = self.browser.find_element(*RegisterPagesLocators.YEAR_DOC_VALIDITY_OPTION)
        year_doc_validity_option.click()
        assert True