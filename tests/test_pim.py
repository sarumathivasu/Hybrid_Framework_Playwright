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
    pim.add_employee_details("Deepa","narayanan","Vasuroja",employee_ID)
    pim.create_toggleon_bydynamic()
    pim.after_toggle_on("Deepa_narayanan")
    pim.select_status()
    pim.password_method("V_saru2002@")
    pim.confirm_password_method("V_saru2002@")
    pim.save_button()
    pim.page.wait_for_timeout(5000)
    # expect(pim.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/289")
    # expect(pim.page.get_by_role("textbox",name="firstName")).to_have_text("sri")
    expect(pim.page.get_by_role("textbox", name="First Name")).to_have_value("sriram")
    expect(pim.page.get_by_role("textbox", name="Last Name")).to_have_value("Vasuroja")
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_be_visible()
    expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_have_value(employee_ID)
    expect(pim.create_login_details_toggle).to_be_checked()
    expect(pim.staus).to_be_checked()
    pim.page.wait_for_timeout(5000)