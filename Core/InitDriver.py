# -*- coding=utf-8 -*-
import time

from Core.InitLogger import InitLogger
from Core.InitConfig import InitConfig
from selenium import webdriver


class InitDriver(object):
    __instance = None
    __inited = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.logger = InitLogger.logger
        if not self.__inited:
            self.config = InitConfig()
            self.driver = self.get_driver(self.config.browser_remote, self.config.browser_headless)
            self.driver.get(self.config.xxxx_base_url + self.config.xxxx_ip)
            self.__inited = True

    def get_driver(self, remote, headless):
        self.logger.info('Start init webdriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('-no-sandbox')
        # chrome_options.add_argument('--window-size=')
        chrome_options.set_capability('browserName', self.config.browser_browsers_name)
        chrome_options.set_capability('platform', "linux")
        chrome_options.set_capability("headless", headless)

        if remote:
            chrome_options.set_capability('version', self.config.browser_remote_version)
            driver = webdriver.Remote(command_executor=self.config.browser_remote_url,
                                      options=chrome_options)
            driver.implicitly_wait(10)
            driver.set_window_size(self.config.browser_window_size_width, self.config.browser_window_size_height)

            self.logger.info('Webdriver init success!')
            return driver
        else:
            chrome_options.set_capability('version', self.config.browser_local_version)
            driver = webdriver.Chrome(executable_path=self.config.browser_chromedriver_path,
                                      options=chrome_options)

            driver.implicitly_wait(10)
            driver.set_window_size(self.config.browser_window_size_width, self.config.browser_window_size_height)

            self.logger.info('Webdriver init success!')
            return driver
