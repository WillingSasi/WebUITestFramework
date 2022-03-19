# -*- coding=utf-8 -*-
import os.path
import yaml
from Core.InitLogger import InitLogger


class InitConfig(object):
    __instance = None
    __inited = False
    config_yaml = os.path.join(os.path.dirname(__file__) + "/../application.yaml")
    pod_id = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.logger = InitLogger.logger
        if not self.__inited:
            self.config_data = self.init_config_yaml(self.config_yaml)
            self.xxxx_base_url = self.config_data['xxxx']['base_url']
            self.xxxx_ip = self.config_data['xxxx']['ip']
            self.auth_username = self.config_data['auth']['username']
            self.auth_password = self.config_data['auth']['password']
            self.browser_chromedriver_path = self.config_data['browser']['chromedriver_path']
            self.browser_browsers_name = self.config_data['browser']['browsers_name']
            self.browser_remote_version = self.config_data['browser']['remote_version']
            self.browser_local_version = self.config_data['browser']['local_version']
            self.browser_window_size_width = self.config_data['browser']['window_size_width']
            self.browser_window_size_height = self.config_data['browser']['window_size_height']
            self.browser_download_dir = self.config_data['browser']['download_dir']
            self.browser_remote_url = self.config_data['browser']['remote_url']
            self.browser_headless = self.config_data['browser']['headless']
            self.browser_remote = self.config_data['browser']['remote']
            self.testframe_name = self.config_data['testframe']['name']
            self.__inited = True

            self.logger.info('Init application.yaml config success!')

    def init_config_yaml(self, config_yaml):
        config_stream = open(config_yaml, encoding="UTF-8")
        config_data = yaml.safe_load(config_stream)

        self.logger.info('Read application.yaml config success!')
        return config_data


if __name__ == '__main__':
    print(InitConfig().config_data)
