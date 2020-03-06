# -*- encoding: utf-8 -*-
'''
@File    :   TestLogin.py
@Time    :   2020/02/11 16:45:27
@Author  :   peace_su
@Version :   1.0
@Contact :   peace_su@163.com
@WebSite :   https://me.csdn.net/u010098760
'''
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# here put the import lib
import unittest
from appium import webdriver
from pages.BasePage import BasePage
from pages.WelcomePage import WelcomePage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from util.LoggingUtil import LoggingUtil
import time
import logging


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.logging_util = LoggingUtil()
        self.logging_util.setup_logging()
        self.logger = logging.getLogger()
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:5554',  # 手机设备名称，通过adb devices查看
            'platformVersion': '5.1.1',  # android系统的版本号
            'appPackage': 'com.aiosign.dzonesign',  # apk包名
            'appActivity': 'com.aiosign.dzonesign.view.AppStartActivity',
            # apk的launcherActivity
        }
        self.logger.info('启动app')
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        self.base_page = BasePage(self.driver)
        self.welcome_page = WelcomePage(self.base_page)
        self.login_page = LoginPage(self.base_page)
        self.main_page = MainPage(self.base_page)

    # def test_right(self):
    #     self.logger.info('开始测试test_right=====================================')
    #     self.base_page.swipe_to_left()
    #     self.base_page.swipe_to_left()
    #     self.welcome_page.click_tiyan_button()
    #     self.welcome_page.click_login_button()
    #     self.login_page.input_username('15628811989')
    #     self.login_page.input_passwd('12345678')
    #     self.login_page.click_signin_button()
    #     # res = self.main_page.is_personal_center_button_exist()
    #     self.main_page.click_personal_center_button()
    #     self.logger.info('测试完成')
    #     # self.assertEqual(res, True)

    def test_login_1(self):
        self.logger.info('开始测试test_login_1==================================')
        self.base_page.swipe_to_left()
        self.base_page.swipe_to_left()
        self.welcome_page.click_tiyan_button()
        self.welcome_page.click_login_button()
        self.login_page.input_username('15628811988')
        self.login_page.input_passwd('12345678')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('用户不存在')
        self.assertEqual(res, True)
        self.logger.info('测试结束=====================================')

    def test_login_2(self):
        self.base_page.swipe_to_left()
        self.base_page.swipe_to_left()
        self.welcome_page.click_tiyan_button()
        self.welcome_page.click_login_button()
        self.login_page.input_username('15628811989')
        self.login_page.input_passwd('123456789')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('账号或密码错误')
        self.assertEqual(res, True)

    '''
    def test_login_3(self):
        self.base_page.swipe_to_left()
        self.base_page.swipe_to_left()
        self.welcome_page.click_tiyan_button()
        self.welcome_page.click_login_button()
        self.login_page.input_username('15628811989')
        # self.login_page.input_passwd('')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('请输入密码！')
        self.assertEqual(res, True)

    def test_login_4(self):
        self.base_page.swipe_to_left()
        self.base_page.swipe_to_left()
        self.welcome_page.click_tiyan_button()
        self.welcome_page.click_login_button()
        self.login_page.input_username('156288119')
        self.login_page.input_passwd('12345678')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('账号格式不正确（邮箱、信用代码、手机）')
        self.assertEqual(res, True)

    def test_login_5(self):
        self.base_page.swipe_to_left()
        self.base_page.swipe_to_left()
        self.welcome_page.click_tiyan_button()
        self.welcome_page.click_login_button()
        # self.login_page.input_username('')
        self.login_page.input_passwd('12345678')
        self.login_page.click_signin_button()
        res = self.base_page.is_toast_exist('请输入账号！')
        self.assertEqual(res, True)
    '''
    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
