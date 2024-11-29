import pytest
import allure
#  pytest --browser=chromium --browser=firefox


@allure.step("Регистрация с уже существующими данными")
@pytest.mark.negative
def test_registration_with_existing_data(create_account_page):
    create_account_page.open()
    create_account_page.field_incorrect_user_name('test_user11')
    create_account_page.field_incorrect_click(' ')
    create_account_page.check_user_nam_error_message('Имя пользователя уже занято')
    create_account_page.clear_field_user_name()


@allure.step('Проверка сообщения поле Имя пользователя')
@pytest.mark.negative
def test_negative_field_incorrect_user_name(create_account_page):
    error_message_data = 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'
    create_account_page.open()
    create_account_page.field_incorrect_user_name('Vlad_')
    create_account_page.check_user_error_message(error_message_data)
    create_account_page.clear_field_user_name()
    create_account_page.field_incorrect_user_name('Влад')
    create_account_page.check_user_error_message(error_message_data)
    create_account_page.clear_field_user_name()
    create_account_page.field_incorrect_user_name('The_number_of_characters_is_more_than_32')
    create_account_page.check_user_error_message(error_message_data)
    create_account_page.clear_field_user_name()
    create_account_page.field_special_character('$')
    create_account_page.check_user_name_error_message('Введены недопустимые символы')


@allure.step('Проверка сообщения поле Электронная почта')
@pytest.mark.negative
def test_negative_field_incorrect_email(create_account_page):
    error_message_data = 'Формат e-mail: username@test.ru'
    create_account_page.open()
    create_account_page.field_incorrect_email('v@имейл.ру')
    create_account_page.check_email_error_message(error_message_data)
    create_account_page.clear_field_email()
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


@allure.step('Проверка сообщения поле Пароль')
@pytest.mark.negative
def test_negative_field_incorrect_password(create_account_page):
    password_data = ('The_password_must_contain_from_8_to_64_characters,'
                     ' including_capital_letters_and_numbers')
    create_account_page.open()
    create_account_page.field_incorrect_password('A123456')
    create_account_page.check_password_error_message_min('Пароль должен содержать минимум 8 символов')
    create_account_page.clear_field_password()
    create_account_page.field_incorrect_password(password_data)
    create_account_page.check_password_error_message_max('Пароль должен содержать от 8 до 64 символов,'
                                                         ' включая заглавные буквы и цифры')
    create_account_page.clear_field_password()
    create_account_page.field_incorrect_password('Влад1234567')
    create_account_page.select_checkbox()
    create_account_page.press_next()
    create_account_page.check_password_error_message_max('Пароль должен содержать от 8 до 64 символов,'
                                                         ' включая заглавные буквы и цифры')


@allure.step('Проверка сообщения поле Реферальный код')
@pytest.mark.negative
def test_negative_field_referral_code(create_account_page):
    error_message_data = 'Неверный формат ссылки'
    create_account_page.open()
    create_account_page.field_incorrect_referral_code('A12')
    create_account_page.check_referral_code_error_message(error_message_data)
    create_account_page.clear_field_referral_code()
    create_account_page.field_incorrect_referral_code('A1234567$')
    create_account_page.check_referral_code_error_message(error_message_data)
    create_account_page.clear_field_referral_code()


@allure.step("Проверка сообщения Не заполненные поля")
@pytest.mark.negative
def test_with_empty_fields(create_account_page):
    create_account_page.open()
    create_account_page.select_checkbox()
    create_account_page.press_next()
    create_account_page.check_with_empty_fields('Поле не заполнено')
