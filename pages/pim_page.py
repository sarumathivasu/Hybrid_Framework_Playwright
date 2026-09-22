from playwright.sync_api import Page
from pages.base_page import BasePage


class PimPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.click_pim=page.get_by_text("PIM",exact=True)
        self.click_add_employee=page.get_by_role("button",name="Add")
        self.first_name=page.get_by_placeholder("First Name")
        self.middle_name=page.get_by_placeholder("Middle Name")
        self.last_name=page.get_by_placeholder("Last Name")
        self.employee_id = page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")
        self.create_login_details_toggle = page.locator(".oxd-switch-wrapper .oxd-switch-input")
        self.create_login_details_checkbox = page.locator(".oxd-switch-wrapper input[type='checkbox']")

        self.username=page.locator('label.oxd-label:has-text("Username")').locator("xpath=../following-sibling::div//input")
        self.staus=page.locator(".oxd-radio-wrapper .oxd-radio-input ").nth(0)
        self.password=page.locator("label.oxd-label:text-is('Password')").locator("xpath=../following-sibling::div//input")
        self.confirm_password=page.locator("label.oxd-label:has-text('Confirm Password')").locator("xpath=../following-sibling::div//input")
    

        self.save=page.get_by_role("button",name="Save")
        

    def click_pim_button(self):
        self.click_pim.click()
    def click_add_employee_button(self):
        self.click_add_employee.click()
    def add_employee_details(self,first_name,middle_name,last_name,employee_id):
        self.first_name.fill(first_name)
        self.middle_name.fill(middle_name)
        self.last_name.fill(last_name)
        self.employee_id.clear()
        self.employee_id.fill(employee_id)

    def create_toggleon_bydynamic(self):
        if not self.create_login_details_checkbox.is_checked():
            self.create_login_details_toggle.click()
    def after_toggle_on(self,username):
        self.username.fill(username)

    def select_status(self):
        self.staus.click()

    def password_method(self,password):
        self.password.fill(password)

    def confirm_password_method(self,confirm_password):
        self.confirm_password.fill(confirm_password)

    def save_button(self):
        self.save.click()
    
