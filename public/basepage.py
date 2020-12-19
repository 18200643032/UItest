# @Time : 2020/12/8 16:24 
# @modele : basepage
# @Author : zhengzhong
# @Software: PyCharm
import yaml
from docs.config import *
class Page():
    def __init__(self, selenium_driver):
        self.dr = selenium_driver
        with open(config_yaml_path, "r", encoding="utf-8") as file:
            a1 = file.read()
        self.index = yaml.load(a1,Loader=yaml.FullLoader)