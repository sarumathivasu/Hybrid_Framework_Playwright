from playwright.sync_api import Page,expect
from pages.pim_page import PimPage
from test_data.employee_details import First_name,Last_name,employee_ID,user_name,password,confirm_password

def test_add_employee_details(login_page,trace_on_failure):

    pim=PimPage(login_page.page)

    pim.click_pim_button()
    expect(pim.page.get_by_role("heading",name="PIM")).to_be_visible()
    pim.click_add_employee_button()

    expect(pim.page.get_by_role("heading",name="Add Employee")).to_be_visible()
    
    pim.add_employee_details(First_name,Last_name,"Vasuroja",employee_ID)
    pim.create_toggleon_bydynamic()
    pim.after_toggle_on(user_name)
    pim.select_status()
    pim.password_method(password)
    pim.confirm_password_method(confirm_password)
    pim.save_button()
    pim.page.wait_for_timeout(5000)
    # print("URL:", pim.page.url)
    # print("Errors:", pim.page.locator(".oxd-input-field-error-message").all_inner_texts())

    pim.search_navigation()
    pim.search_employee_id(employee_ID)
    pim.search_button_method()

    # # expect(pim.page.get_by_role("textbox", name="First Name")).to_have_value(first_name)
    # expect(pim.page.get_by_role("textbox", name="Last Name")).to_have_value("Vasuroja")
    # expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_be_visible()
    # expect(pim.page.locator('label.oxd-label:has-text("Employee Id")').locator("xpath=../following-sibling::div//input")).to_have_value(employee_ID)
    # expect(pim.create_login_details_toggle).to_be_checked()
    # expect(pim.staus).to_be_checked()
    expect(pim.page.locator("body")).to_contain_text("(1) Record Found")

