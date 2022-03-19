# -*- coding:utf-8 -*-
import os
import time
from pathlib import Path

import allure
from selenium.webdriver import ActionChains

from Core.InitConfig import InitConfig
from Core.InitLogger import InitLogger
from selenium.webdriver.support.wait import WebDriverWait

screenshot_path = os.path.join(os.path.dirname(__file__))


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """

    def __init__(self, driver):
        self.driver = driver
        self.logger = InitLogger.logger
        self.config = InitConfig()

    @allure.step
    def find_element(self, *element):
        self.logger.info("Find Element")
        web_element = self.driver.find_element(*element)
        self.screenshot()
        return web_element

    @allure.step
    def find_elements(self, *element):
        self.logger.info("Find Elements")
        web_elements = self.driver.find_elements(*element[1:])
        self.screenshot()
        return web_elements

    @allure.step
    def send_keys(self, keys, *element):
        self.logger.info("Start Send Keys")
        web_element = self.find_element(*element[1:])
        self.screenshot()
        web_element.send_keys(*element[0])
        self.logger.info("Send Keys Success!")

    @allure.step
    def click(self, *element):
        self.logger.info("Start Click Element")
        web_element = self.find_element(*element[1:])
        if web_element.is_displayed():
            web_element.click()
            self.logger.info("Click Element Success!")
        else:
            self.logger.warning("Element Not Displayed!")

    @allure.step
    def move_to_element(self, *element):
        self.logger.info("Start Hover Element")
        web_element = self.find_element(*element[1:])
        ActionChains(self.driver).move_to_element(web_element).perform()
        self.logger.info("Hover Element Success!")

    @allure.step
    def reset_action_chains(self):
        self.logger.info("Reset Action Chains")
        ActionChains(self.driver).reset_actions()
        self.logger.info("Reset Action Chains Success!")

    @allure.step
    def get_text(self, *element):
        self.logger.info("Start Get Text Element")
        web_element = self.find_element(*element[1:])
        text = web_element.text
        self.logger.info("Get Text Success! Text : " + text)
        return text

    @allure.step
    def execute_script(self, script, *args):
        self.logger.info("JS Execute Script")
        web_elements = self.driver.execute_script(self, script, *args)
        self.screenshot()
        return web_elements

    def screenshot(self):
        image_name = screenshot_path + '/' + str(time.time()) + '.png'
        self.driver.get_screenshot_as_file(image_name)
        allure.attach.file(image_name, attachment_type=allure.attachment_type.PNG)
        self.logger.info("Save Screenshot Success!")

    def dynamic_wait(self, condition, times):
        num = 0
        while condition is False and num < times:
            time.sleep(1)
            num += 1

        return condition
