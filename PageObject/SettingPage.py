# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class SettingPage(BasePage):
    _connect = (By.XPATH, 'xxxx')
    _cancel = (By.XPATH, 'xxxx')

    def click_connect(self):
        self.click(self, *self._connect)
        return self

    def click_cancel(self):
        self.click(self, *self._cancel)
        return self

