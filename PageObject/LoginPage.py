# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class LoginPage(BasePage):
    _username = (By.ID, 'xxxx')
    _password = (By.ID, 'xxxx')
    _login_button = (By.NAME, 'xxxx')

    def username_input(self, username):
        self.send_keys(self, username, *self._username)
        return self

    def password_input(self, password):
        self.send_keys(self, password, *self._password)
        return self

    def login_button_click(self):
        self.click(self, *self._login_button)
        return self
