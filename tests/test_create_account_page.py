import pytest
import allure


@allure.step('Поле "Имя пользователя"')
@pytest.mark.negative
@pytest.mark.regression
def test_negative_field_incorrect_user_name(create_account_page):
    error_message_data = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
    create_account_page.open()
    create_account_page.create_account()
    create_account_page.field_incorrect_user_name('Vlad_')
    create_account_page.check_user_error_message(error_message_data)
    create_account_page.clear_field_user_name()
    create_account_page.field_incorrect_user_name('The_number_of_characters_is_more_than_32')
    create_account_page.check_user_error_message(error_message_data)
    create_account_page.clear_field_user_name()
    create_account_page.field_special_character('$')
    create_account_page.check_user_name_error_message('Введены недопустимые символы')


@allure.step('Поле "Электронная почта"')
@pytest.mark.negative
@pytest.mark.regression
def test_negative_field_incorrect_email(create_account_page):
    error_message_data = 'Формат e-mail: username@test.ru'
    create_account_page.open()
    create_account_page.create_account()
    create_account_page.field_incorrect_email('email.ru')
    create_account_page.check_email_error_message(error_message_data)
    create_account_page.clear_field_email()
    create_account_page.field_incorrect_email('@email.ru')
    create_account_page.check_email_error_message(error_message_data)
    create_account_page.clear_field_email()
    create_account_page.field_incorrect_email('@@email.ru')
    create_account_page.check_email_error_message(error_message_data)
    create_account_page.clear_field_email()
    create_account_page.field_incorrect_email('V@emailru')
    create_account_page.check_email_error_message(error_message_data)
    create_account_page.clear_field_email()
    create_account_page.field_incorrect_email('V@email.r')
    create_account_page.check_email_error_message(error_message_data)


@allure.step('Поле "Пароль"')
@pytest.mark.negative
@pytest.mark.regression
def test_negative_field_incorrect_password(create_account_page):
    password_data = ('The password must contain from 8 to 64 characters,'
                     ' including capital letters and numbers')
    create_account_page.open()
    create_account_page.create_account()
    create_account_page.field_incorrect_password('A123456')
    create_account_page.check_password_error_message_min('Пароль должен содержать минимум 8 символов')
    create_account_page.clear_field_password()
    create_account_page.field_incorrect_password(password_data)
    create_account_page.check_password_error_message_max('Пароль должен содержать от 8 до 64 символов,'
                                                         ' включая заглавные буквы и цифры')
    create_account_page.clear_field_password()


@allure.step('Поле "Реферальный код"')
@pytest.mark.negative
@pytest.mark.regression
def test_negative_field_referral_code(create_account_page):
    error_message_data = 'Неверный формат ссылки'
    create_account_page.open()
    create_account_page.create_account()
    create_account_page.field_incorrect_referral_code('A12')
    create_account_page.check_referral_code_error_message(error_message_data)
    create_account_page.clear_field_referral_code()
    create_account_page.field_incorrect_referral_code('A1234567$')
    create_account_page.check_referral_code_error_message(error_message_data)
    create_account_page.clear_field_referral_code()
