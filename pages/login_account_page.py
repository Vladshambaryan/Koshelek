from time import sleep

from locators import create_account_locators as loc
from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginAccount(BasePage):

    page_url = '/authorization/login'

    def field_incorrect_user_name(self, text):
        field = self.page.get_by_label(loc.field_loc)
        field.press_sequentially(text)
        field.press('Enter')

    def field_special_character(self, text):
        field = self.page.get_by_label(loc.field_loc)
        field.press_sequentially(text)

    def clear_field_user_name(self):
        field = self.page.get_by_label(loc.field_loc)
        field.click()
        field.press("Control+A")
        field.press("Backspace")

    def check_user_error_message(self, text):
        expect(self.page.get_by_text(loc.mes_error)).to_have_text(text)

    def check_user_name_error_message(self, text):
        expect(self.page.get_by_text(loc.mess_error)).to_contain_text(text)


    def field_incorrect_email(self, text):
        field = self.page.get_by_label(loc.email_loc)
        field.press_sequentially(text)
        field.press('Enter')

    def clear_field_email(self):
        field = self.page.get_by_label(loc.email_loc)
        field.click()
        field.press("Control+A")
        field.press("Backspace")

    def check_email_error_message(self, text):
        expect(self.page.get_by_text(loc.email_error_loc)).to_have_text(text)


    def field_incorrect_password(self, text):
        field = self.page.get_by_label(loc.password_loc)
        field.press_sequentially(text)
        field.press('Enter')

    def clear_field_password(self):
        field = self.page.get_by_label(loc.password_loc)
        field.click()
        field.press("Control+A")
        field.press("Backspace")

    def check_password_error_message(self, text):
        expect(self.page.get_by_text(loc.password_error_message___loc)).to_contain_text(text)


    def press_in(self):
        press_next = self.page.get_by_text(loc.in_loc)
        press_next.click()

    def check_with_empty_fields(self, text):
        elements = self.page.get_by_text(loc.empty_fields_loc)
        assert elements.count() == 2
        for i in range(elements.count()):
            element = elements.nth(i)
            assert element.is_visible()
            assert element.inner_text() == text