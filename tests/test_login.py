import pytest
from drivers.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()
    assert "Dashboard" in driver.page_source
