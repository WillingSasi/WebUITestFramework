# -*- coding=utf-8 -*-
import time

import allure

from TestScript.BaseCase import BaseCase
import pytest

from Utils.ApiUtil import get_latest_image_tag


class TestLoginInfoVerify(BaseCase):

    def login_info_verify(self):
        self.loginPage\
            .username_input(self.config.auth_username)\
            .password_input(self.config.auth_password)\
            .login_button_click()

        time.sleep(10)


if __name__ == '__main__':
    TestLoginInfoVerify().login_info_verify()
