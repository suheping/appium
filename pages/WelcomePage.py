# -*- encoding: utf-8 -*-
'''
@File    :   WelcomePage.py
@Time    :   2020/02/11 14:49:29
@Author  :   peace_su
@Version :   1.0
@Contact :   peace_su@163.com
@WebSite :   https://me.csdn.net/u010098760
'''

# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class WelcomePage(BasePage):
    '''欢迎页面元素及方法
        该类继承自BasePage类

    Attributes:
        属性说明
    '''
    # 立即体验 按钮
    tiyan_button = (By.ID, 'com.aiosign.dzonesign:id/vStartNow')

    # 登录 按钮
    login_button = (By.ID, 'com.aiosign.dzonesign:id/btLoginUser')

    # 注册 按钮
    register_button = (By.ID, 'com.aiosign.dzonesign:id/btRegisterUser')

    # 点击立即体验按钮
    def click_tiyan_button(self):
        self.find_element(*self.tiyan_button).click()

    # 点击登录按钮
    def click_login_button(self):
        self.find_element(*self.login_button).click()

    # 点击注册按钮
    def click_register_button(self):
        self.find_element(*self.register_button).click()


if __name__ == '__main__':
    print(123)
