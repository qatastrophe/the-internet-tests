import re

from playwright.sync_api import Page, expect
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.secure_page import SecurePage


@pytest.mark.login
class TestLogin:
    def test_successefull_login(
        self,
        page: Page,
        main_page: MainPage,
        login_page: LoginPage,
        secure_page: SecurePage,
        secure_credentials,
    ):
        page.goto("/")

        main_page.open("Form Authentication")

        login_page.login_with(
            secure_credentials["user"], secure_credentials["password"]
        )

        expect(page, "URL should contain /secure in its path").to_have_url(
            re.compile(".*/secure")
        )
        expect(
            secure_page.logged_in_msg,
            "Message should be 'You logged into a secure area!'",
        ).to_have_text(re.compile("You logged into a secure area!"))

    @pytest.mark.parametrize(
        "test_case",
        (
            pytest.param(
                {
                    "user": "tomsmith",
                    "password": "invalidpass",
                    "error_message": "Your password is invalid!",
                },
                id="invalid password",
            ),
            pytest.param(
                {
                    "user": "tomsmith",
                    "password": "",
                    "error_message": "Your password is invalid!",
                },
                id="blank password",
            ),
            pytest.param(
                {
                    "user": "nonexist",
                    "password": "pass123",
                    "error_message": "Your username is invalid!",
                },
                id="non-exist user",
            ),
            pytest.param(
                {
                    "user": "",
                    "password": "",
                    "error_message": "Your username is invalid!",
                },
                id="both blank username and password",
            ),
        ),
    )
    def test_invalid_login(
        self, page: Page, login_page: LoginPage, test_case
    ):

        login_page.goto()

        login_page.fill_username(test_case["user"])
        login_page.fill_password(test_case["password"])
        login_page.click_login_button()

        expect(
            login_page.flash_message, f"Message should be {test_case['error_message']}"
        ).to_have_text(re.compile(test_case["error_message"]))
        expect(
            login_page.flash_message, "Message should contain class 'error'"
        ).to_contain_class("error")
        expect(page).not_to_have_url(re.compile(".*/secure"))

    def test_logout(
        self, login_page: LoginPage, secure_page: SecurePage, secure_credentials
    ):

        login_page.goto()
        login_page.login_with(
            secure_credentials["user"], secure_credentials["password"]
        )

        expect(secure_page.page, "URL should contain /secure in its path").to_have_url(
            re.compile(".*/secure")
        )
        expect(
            secure_page.logged_in_msg,
            "Message should be 'You logged into a secure area!'",
        ).to_have_text(re.compile("You logged into a secure area!"))
        expect(secure_page.content_block).to_be_visible()

        secure_page.click_logout()
        expect(login_page.username_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.page, "URL should contain /secure in its path").to_have_url(
            re.compile(".*/login")
        )
