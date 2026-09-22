from helpers.locators import LOGIN_BUTTON, LOGIN_EMAIL_INPUT, PASSWORD_INPUT
from pages.base_page import BasePage


class LoginPage(BasePage):

    def set_email(self, email):
        self.set_value(LOGIN_EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_value(PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)