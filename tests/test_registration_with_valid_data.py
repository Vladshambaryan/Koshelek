from playwright.sync_api import BrowserContext
import pytest


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    playwright.chromium.launch(headless=True)
    page = context.new_page()
    page.set_viewport_size({'width': 1700, 'height': 980})
    return page


def test_registration_with_valid_data(page):
    page.goto('https://koshelek.ru/authorization/signup')
    name = page.get_by_label('Имя пользователя')
    name.press_sequentially('test_user111')
    email = page.get_by_label('Электронная почта')
    email.press_sequentially('skachat30913@gmail.com')
    password = page.get_by_label('Пароль')
    password.press_sequentially('m88439ut98#^%ry*&^%098-L<N<MB')
    ref_code =page.get_by_label('Реферальный код')
    ref_code.press_sequentially('A1234567')
    check_box = page.get_by_role("checkbox")
    check_box.click()
    press_next = page.get_by_text('Далее')
    press_next.click()
    assert page.url == "https://koshelek.ru/authorization/signup"
    try:
        recaptcha_frame = page.frame_locator("iframe[src*='recaptcha']")
        if recaptcha_frame:
            print("Рекапча присутствует на странице.")
        else:
            print("Рекапча отсутствует на странице.")
    except Exception as e:
        print("Ошибка при проверке рекапчи:", e)


def test_create_new_wallet(page):
    page.goto("https://koshelek.ru/authorization/login")
    email = page.get_by_label('Электронная почта')
    email.press_sequentially('skachat30913@gmail.com')
    password = page.get_by_label('Пароль')
    password.press_sequentially('m88439ut98#^%ry*&^%098-L<N<MB')
    press_next = page.get_by_role("button", name="Войти")
    press_next.click()
    assert page.url == "https://koshelek.ru/authorization/login"
    try:
        recaptcha_frame = page.frame_locator("iframe[src*='recaptcha']")
        if recaptcha_frame:
            print("Рекапча присутствует на странице.")
        else:
            print("Рекапча отсутствует на странице.")
    except Exception as e:
        print("Ошибка при проверке рекапчи:", e)
