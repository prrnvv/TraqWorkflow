from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = (By.XPATH, "//input[contains(@placeholder,'Username')]")
    _password_input = (By.XPATH, "//input[contains(@aria-placeholder,'Password')]")
    _login_button = (By.ID, "validateSubmit")

    def enter_username(self, username):
        self.enter_text(self._username_input, username)

    def enter_password(self, password):
        self.enter_text(self._password_input, password)

    def click_login(self):
        self.click(self._login_button)
