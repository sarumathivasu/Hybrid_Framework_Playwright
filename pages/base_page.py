# Import Playwright's Page type.
# This is used for type hinting and tells Python
# that 'page' is a Playwright Page object.
from playwright.sync_api import Page


# BasePage contains common actions
# that can be reused by all Page Objects.
class BasePage:

    # Constructor.
    # It receives the Playwright page object.
    def __init__(self, page: Page):

        # Store the Playwright page object
        # so other methods can use self.page.
        self.page = page

    # Common navigation method.
    # Any Page Object can use this method.
    def navigate(self, url):

        # Open the given URL in the browser.
        self.page.goto(url)

    # Common click method.
    # Any Page Object can reuse this.
    def click(self, locator):

        # Click the locator passed to this method.
        locator.click()

    # Common fill method.
    # Any Page Object can reuse this.
    def fill(self, locator, value):

        # Fill the locator with the given value.
        locator.fill(value)
