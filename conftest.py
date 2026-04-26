import os

import dotenv
from playwright.sync_api import Page
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.secure_page import SecurePage

dotenv.load_dotenv()

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
