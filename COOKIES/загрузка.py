import os
import pickle
from time import sleep

from playwright.sync_api import sync_playwright

def test_load_and_apply_cookies():
    with sync_playwright() as p:
        # Открываем браузер и запускаем страницу
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открытие страницы и удаление всех кук
        page.goto("https://koshelek.ru/authorization/login")
        context.clear_cookies()  # Удаление всех кук текущего контекста
        # Загрузка кук из файла и добавление их в текущий контекст
        cookies_path = os.path.join(os.getcwd(), "cookie_file/cookies.pkl")
        with open(cookies_path, "rb") as cookie_file:
            cookies = pickle.load(cookie_file)
            context.add_cookies(cookies)

        # Обновление страницы для применения кук и автоматического входа
        page.reload()
        sleep(40)
