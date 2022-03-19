# -*- coding:utf-8 -*-
import logging.config
import os
import time
from pathlib import Path
import yaml


class InitLogger(object):
    __instance = None
    __inited = False
    logger_yaml = os.path.join(os.path.dirname(__file__) + "/../Conf/logger.yaml")
    logger = logging.getLogger('simpleExample')

    def __new__(cls, *args, **kwargs):
        if InitLogger.__instance is None:
            InitLogger.__instance = object.__new__(cls)
        return InitLogger.__instance

    def __init__(self, testcase_log_dir):
        if not InitLogger.__inited:
            config_stream = open(self.logger_yaml, encoding="UTF-8")
            dict_conf = yaml.safe_load(config_stream)
            dict_conf['handlers']['info_file_handler']['filename'] = testcase_log_dir + '/run.log'
            dict_conf['handlers']['error_file_handler']['filename'] = testcase_log_dir + '/error.log'
            # dict_conf['handlers']['console_debug']['filename'] = testcase_log_dir + '/console.log'

            logging.config.dictConfig(dict_conf)
            self.logger = logging.getLogger('simpleExample')

            self.logger.info('Log init Success!')
            self.__inited = True


# if __name__ == "__main__":
    # init_logger = InitLogger(testcase_log_dir).logger
    # init_logger.debug("test debug log!")
    # init_logger.info("test info log!")
    # init_logger.warning("test warning log!")
    # init_logger.error("test error log!")
