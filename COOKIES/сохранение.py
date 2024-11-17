import pickle
import os
from time import sleep

from playwright.sync_api import sync_playwright


def test_login_with_cookies():
    with sync_playwright() as p:
        # Открываем браузер и запускаем страницу
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://koshelek.ru/authorization/login")

        email = page.get_by_label('Электронная почта')
        email.press_sequentially('skachat30913@gmail.com')
        password = page.get_by_label('Пароль')
        password.press_sequentially('m88439ut98#^%ry*&^%098-L<N<MB')
        press_next = page.get_by_role("button", name="Войти")
        press_next.click()

        # page.wait_for_load_state('networkidle')
        sleep(20)
        page.reload()
        # Сохраняем куки после авторизации
        cookies_path = os.path.join(os.getcwd(), "cookie_file/cookies.pkl")
        with open(cookies_path, "wb") as cookie_file:
            pickle.dump(context.cookies(), cookie_file)
