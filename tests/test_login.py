from pages.login import Herokyu
import pytest
@pytest.fixture
def login_page(driver):
    login = Herokyu(driver)
    login.open()
    return login
def test_valid_login(login_page):
    secure = login_page.loginWeb("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in secure.get_success_message()
    assert "/secure" in secure.get_current_url()

@pytest.mark.parametrize("username,password,expected",[
    ("tomsmith", "wrongPassword", "Your password is invalid!"),
    ("wrongUser", "SuperSecretPassword!", "Your username is invalid!")
])
def test_invalid_logins(login_page, username, password, expected):
    login_page.loginWeb(username,password)
    assert expected in login_page.get_error_message()
def test_logout(login_page):
    secure = login_page.loginWeb("tomsmith", "SuperSecretPassword!")
    login = secure.click_logout()
    assert "You logged out of the secure area!" in login.get_error_message()