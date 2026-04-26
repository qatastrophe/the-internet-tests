from pages.base_page import BasePage


class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.logged_in_msg = page.locator("#flash")
        self.content_block = page.locator("#content")
        self.logout_btn = page.locator("a[href='/logout']")

    def click_logout(self):
        self.logout_btn.click()
