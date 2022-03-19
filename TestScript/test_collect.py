# -*- coding=utf-8 -*-
import os
from pathlib import Path

import allure

from Core.InitConfig import InitConfig
from Core.InitDriver import InitDriver
from Core.InitLogger import InitLogger
from PageObject import BasePage
from TestScript.BaseCase import BaseCase
from TestScript.TestLoginInfoVerify import TestLoginInfoVerify
from Utils.ApiUtil import xxxx
from Utils.FormatTime import data_time_english_no_delimiter


@allure.feature('xxxx Smoke Test')
class TestCollect:
    result_path = os.path.join(os.path.dirname(__file__) + "/../result")

    @allure.story("login界面异常验证1")
    def test_smoke_one(self):
        TestLoginInfoVerify().login_info_verify()

    def setup_method(self):
        # 初始化日志文件夹
        if not Path(self.result_path).is_dir():
            os.mkdir(self.result_path)
        testcase_log_dir = os.path.join(self.result_path + '/TestLog' + data_time_english_no_delimiter())
        os.mkdir(testcase_log_dir)

        # 初始化全局日志
        self.logger = InitLogger(testcase_log_dir).logger
        BasePage.screenshot_path = testcase_log_dir

        self.logger.info('-----------------Start test case-----------------')

    def teardown_method(self):
        self.logger.info('Quit web Session')
        InitDriver().driver.quit()
        # del InitDriver
        # del BaseCase
        # InitDriver().__instance = None
        # InitDriver().__inited = False
        # BaseCase().__instance = None
        # BaseCase().__inited = False
        xxxx(InitConfig().pod_id, InitConfig().auth_username)
        self.logger.info('-----------------End test case-----------------')
