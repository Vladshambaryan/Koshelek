from playwright.sync_api import BrowserContext
from pages.create_account_page import CreateAccount
from pages.login_account_page import LoginAccount
import pytest


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    playwright.chromium.launch(headless=True)
    page = context.new_page()
    page.set_viewport_size({'width': 1700, 'height': 980})
    return page


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)

@pytest.fixture()
def login_account_page(page):
    return LoginAccount(page)
