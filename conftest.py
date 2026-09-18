from playwright.sync_api import Page
from pages.login_page import LoginPage
import pytest
from test_data.user_login_details import USERNAME,PASSWORD

@pytest.fixture
def login_page(page:Page):
    orange_HRM=LoginPage(page)
    orange_HRM.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    orange_HRM.login(USERNAME,PASSWORD)
    return orange_HRM
