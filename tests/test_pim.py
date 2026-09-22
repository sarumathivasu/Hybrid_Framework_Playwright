from playwright.sync_api import Page,expect
from pages.pim_page import PimPage
from utilities.helpers import generate_unique_empID,generate_unique_first_name

def test_add_employee_details(login_page):

    pim=PimPage(login_page.page)

    pim.click_pim_button()
    expect(pim.page.get_by_role("heading",name="PIM")).to_be_visible()
    pim.click_add_employee_button()

    expect(pim.page.get_by_role("heading",name="Add Employee")).to_be_visible()

    first_name=f"Saru{generate_unique_first_name()}"

    employee_ID=f"EMP{generate_unique_empID()}"

    pim.add_employee_details(first_name,"narayanan","Vasuroja",employee_ID)
    pim.create_toggleon_bydynamic()
    pim.after_toggle_on("Deepa_narayanan")
    pim.select_status()
    pim.password_method("V_saru2002@")
    pim.confirm_password_method("V_saru2002@")
    pim.save_button()

    expect(pim.page.get_by_role("textbox", name="First Name")).to_have_value(first_name)
    expect(pim.page.get_by_role("textbox", name="Last Name")).to_have_value("Vasuroja")
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_be_visible()
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_have_value(employee_ID)
    expect(pim.create_login_details_toggle).to_be_checked()
    expect(pim.staus).to_be_checked()

