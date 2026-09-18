from playwright.sync_api import Page,expect,Playwright
def test_login(login_page):
    # assert "dashboard/index" in login_page.page.url
    expect(login_page.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    # expect(login_page.page.get_by_text("Dashboard")).to_be_visible()
    expect(login_page.page.get_by_role("heading",name="Dashboard")).to_be_visible()