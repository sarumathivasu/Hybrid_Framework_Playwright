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
        self.save=page.get_by_role("button",name="Save")

    def click_pim_button(self):
        self.click_pim.click()
    def click_add_employee_button(self):
        self.click_add_employee.click()
    def add_employee_details(self,first_name,middle_name,last_name):
        self.first_name.fill(first_name)
        self.middle_name.fill(middle_name)
        self.last_name.fill(last_name)
    def save_button(self):
        self.save.click()
    
