from pages.base_page import BasePage


class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.logged_in_msg = page.locator("#flash")
