from playwright.sync_api import Page, expect


class TestMainPage:

    def test_main_page_links(self, page: Page):

        page.goto('https://the-internet.herokuapp.com')

        expect(page).to_have_title("The Internet")