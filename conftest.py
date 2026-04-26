

from playwright.sync_api import Page
import pytest

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def main_page(page: Page):
    yield MainPage(page)