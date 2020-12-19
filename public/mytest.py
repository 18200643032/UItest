import unittest
from public import pyselenium
from public.log import Log
import yaml
from docs.config import *


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium()
        self.dr.max_window()

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')


class Login(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        file = open(config_yaml_path, "r", encoding="utf-8")
        a1 = file.read()
        self.index = yaml.load(a1,Loader=yaml.FullLoader)
        self.logger = Log()
        self.logger.info('############################### Login ###############################')
        self.dr = pyselenium.PySelenium()
        self.dr.max_window()
        self.login()

    def login(self):
        self.dr.open(self.index["index"]["url"])
        self.dr.click(self.index["index"]["zhong_login"])
        self.dr.send_key(self.index["login"]["login_username"], "zheng3")
        self.dr.send_key(self.index["login"]["login_password"], "123456")
        self.dr.click(self.index["login"]["login_sumbit"])

    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')