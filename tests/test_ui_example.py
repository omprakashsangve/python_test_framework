from core.base_ui import BaseUI
from pages.login_page import LoginPage

def test_ui_login():
    ui = BaseUI()
    driver = ui.setup_browser()

    login_page = LoginPage(driver)
    login_page.enter_username("admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    assert "dashboard" in driver.current_url

    ui.teardown_browser()