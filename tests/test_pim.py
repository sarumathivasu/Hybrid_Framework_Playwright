from playwright.sync_api import Page,expect
from pages.pim_page import PimPage
from utilities.helpers import generate_unique_empID

def test_add_employee_details(login_page):

    pim=PimPage(login_page.page)

    pim.click_pim_button()
    expect(pim.page.get_by_role("heading",name="PIM")).to_be_visible()
    pim.click_add_employee_button()
    # expect(pim.page).to_contain_text("Add Employee")
    expect(pim.page.get_by_role("heading",name="Add Employee"))
    employee_ID=f"EMP{generate_unique_empID()}"
    pim.add_employee_details("sriram","narayanan","Vasuroja",employee_ID)
    pim.save_button()
    # expect(pim.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/289")
    # expect(pim.page.get_by_role("textbox",name="firstName")).to_have_text("sri")
    expect(pim.page.get_by_role("textbox", name="First Name")).to_have_value("sriram")
    expect(pim.page.get_by_role("textbox", name="Last Name")).to_have_value("Vasuroja")
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_be_visible()
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_have_value(employee_ID)
    