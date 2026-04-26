from playwright.sync_api import Page, expect

from pages.main_page import MainPage


class TestMainPage:
    def test_main_page(self, page: Page, main_page: MainPage):

        page.goto("https://the-internet.herokuapp.com")

        expect(page, 'The title must be: "The internet"').to_have_title("The Internet")

        expect(
            main_page.github_fork_btn, "Fork me on Github button should be visible"
        ).to_be_visible()
        expect(
            main_page.content_links, "Main page should have exacly 44 links"
        ).to_have_count(44)
