from pages.base_page import BasePage


class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_btn = page.locator('button[type="submit"]')
        self.flash_message = page.locator("#flash")

    def fill_username(self, username: str) -> None:
        self.username_input.fill(username)
    
    def fill_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_btn.click()

    def login_with(self, username: str, password: str) -> None:
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
