# Import Playwright Page type.
from playwright.sync_api import Page

# Import our BasePage.
# LoginPage will inherit from BasePage.
from pages.base_page import BasePage




# LoginPage represents the OrangeHRM login page.
# BasePage is the parent class.
class LoginPage(BasePage):

    # Constructor.
    def __init__(self, page: Page):

        # Call BasePage's constructor.
        # This stores the Playwright page inside self.page.
        super().__init__(page)

        # Locate the username input.
        self.username = page.get_by_placeholder("Username")

        # Locate the password input.
        self.password = page.get_by_placeholder("Password")

        # Locate the Login button.
        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )


    # This method represents the login action.
    def login(self, username, password):

        # Enter username.
        self.username.fill(username)

        # Enter password.
        self.password.fill(password)

        # Click Login.
        self.login_button.click()