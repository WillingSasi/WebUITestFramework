import time

from PageObject.LoginPage import LoginPage


class LoginAction(LoginPage):

    def login(self):
        self.username_input(self.config.auth_username)\
            .password_input(self.config.auth_password)\
            .login_button_click()
        time.sleep(10)

