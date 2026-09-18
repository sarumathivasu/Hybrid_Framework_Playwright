from playwright.sync_api import Page
from pages.login_page import LoginPage
import pytest

@pytest.fixture
def login_page(page:Page):
    sauce_login=LoginPage(page)
    sauce_login.navigate("https://www.saucedemo.com/")
    return sauce_login
