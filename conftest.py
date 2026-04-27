import os

import dotenv
from playwright.sync_api import Page
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.secure_page import SecurePage

dotenv.load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def base_url():
    url = os.environ.get('PYTEST_BASE_URL')
    if not url:
        url = "https://the-internet.herokuapp.com"
        os.environ['PYTEST_BASE_URL'] = url
    return url

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    return {
        **browser_context_args,
        "base_url": base_url
    }

@pytest.fixture(scope="function")
def main_page(page: Page):
    yield MainPage(page)


@pytest.fixture(scope="function")
def login_page(page: Page):
    yield LoginPage(page)


@pytest.fixture(scope="function")
def secure_page(page: Page):
    yield SecurePage(page)


@pytest.fixture(scope="function")
def secure_credentials():
    user = os.environ.get("USER", "")
    password = os.environ.get("PASSWORD", "")

    if user == "":
        raise Exception("To test with this fixture USER have to be set")

    if password == "":
        raise Exception("To test with this fixture PASSWORD have to be set")


    yield {"user": user, "password": password}
