# @Time : 2020/12/8 18:01 
# @modele : run.py
# @Author : zhengzhong
# @Software: PyCharm
#coding=utf-8

import unittest
import HTMLTestRunner
import time
# from config import globalparam
# from public.common import sendmail
from docs.config import *

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()

if __name__=='__main__':
    run()