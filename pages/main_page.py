from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page

        self.github_fork_btn = page.locator("a[href*=github] img")
        self.content_links = page.locator("#content li a")
        self.content_link = lambda link: page.locator("#content li a", has_text=link)

    def open(self, link: str) -> None:
        links_found_count = self.content_link(link).count()
        if links_found_count == 0:
            raise Exception(f'There is no link with "{link}" title')
        self.content_link(link).click()
