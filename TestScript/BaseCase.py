# -*- coding:utf-8 -*-
import os
import time
from pathlib import Path

from Core.InitConfig import InitConfig
from Core.InitDriver import InitDriver
from Core.InitLogger import InitLogger
from PageObject.BasePage import BasePage
from PageObject.CommonPage import CommonPage
from PageObject.LoginPage import LoginPage
from PageObject.SettingPage import SettingPage
from Utils.ApiUtil import *
from Utils.FormatTime import data_time_english_no_delimiter


class BaseCase(object):
    __instance = None
    __inited = False
    result_path = os.path.join(os.path.dirname(__file__) + "/../result")

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__inited:
            # 初始化日志文件夹
            # if not Path(self.result_path).is_dir():
            #     os.mkdir(self.result_path)
            # testcase_log_dir = os.path.join(self.result_path + '/TestLog' + data_time_english_no_delimiter())
            # os.mkdir(testcase_log_dir)

            # 初始化全局日志
            # self.logger = InitLogger(testcase_log_dir).logger
            # BasePage.screenshot_path = testcase_log_dir

            # 初始化全局配置文件
            self.config = InitConfig()

            # 新建 image
            logger.info("Start create new image")
            logger.info("Create new image success! IP : " + pod_ip)

            # 初始化全局driver
            self.driver = InitDriver().driver
            time.sleep(5)

            # 实例化所有page，action
            self.commonPage = CommonPage(self.driver)
            self.loginPage = LoginPage(self.driver)
            self.settingPage = SettingPage(self.driver)

