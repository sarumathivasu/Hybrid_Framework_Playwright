from playwright.sync_api import Page
from pages.login_page import LoginPage
import pytest
from test_data.user_login_details import USERNAME,PASSWORD
from config.config import BASE_URL

@pytest.fixture
def login_page(page:Page):
    orange_HRM=LoginPage(page)
    orange_HRM.navigate(BASE_URL)
    orange_HRM.login(USERNAME,PASSWORD)
    return orange_HRM

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def trace_on_failure(page, request):
    context = page.context

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield

    test_failed = request.node.rep_call.failed

    if test_failed:
        context.tracing.stop(
            path=f"traces/{request.node.name}.zip"
        )
    else:
        context.tracing.stop()


