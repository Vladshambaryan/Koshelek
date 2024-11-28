import pytest
import allure
from conftest import login_account_page


@allure.step('Проверка сообщения поле "Электронная почта"')
@pytest.mark.negative
def test_negative_field_incorrect_email(login_account_page):
    error_message_data = 'Формат e-mail: username@test.ru'
    login_account_page.open()
    login_account_page.field_incorrect_email('v@имейл.ру')
    login_account_page.check_email_error_message(error_message_data)
    login_account_page.clear_field_email()
    login_account_page.field_incorrect_email('email.ru')
    login_account_page.check_email_error_message(error_message_data)
    login_account_page.clear_field_email()
    login_account_page.field_incorrect_email('@email.ru')
    login_account_page.check_email_error_message(error_message_data)
    login_account_page.clear_field_email()
    login_account_page.field_incorrect_email('@@email.ru')
    login_account_page.check_email_error_message(error_message_data)
    login_account_page.clear_field_email()
    login_account_page.field_incorrect_email('V@emailru')
    login_account_page.check_email_error_message(error_message_data)
    login_account_page.clear_field_email()
    login_account_page.field_incorrect_email('V@email.r')
    login_account_page.check_email_error_message(error_message_data)


@allure.step('Проверка сообщения Пароль должен содержать не менее 8 символов')
@pytest.mark.negative
def test_negative_field_incorrect_password(login_account_page):
    login_account_page.open()
    login_account_page.field_incorrect_password('A12')
    login_account_page.check_password_error_message('Пароль должен содержать не менее 8 символов')


@allure.step("Проверка сообщения Поле не заполнено")
@pytest.mark.negative
def test_with_empty_fields(login_account_page):
    login_account_page.open()
    login_account_page.press_in()
    login_account_page.check_with_empty_fields('Поле не заполнено')

