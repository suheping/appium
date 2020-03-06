# -*- encoding: utf-8 -*-
'''
@File    :   MainPage.py
@Time    :   2020/03/04 16:02:25
@Author  :   peace_su
@Version :   1.0
@Contact :   peace_su@163.com
@WebSite :   https://me.csdn.net/u010098760
'''

# here put the import lib
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    '''主页面元素及方法
    详细描述

    Attributes:
        属性说明
    '''

    # 个人中心按钮
    personal_center_button = (By.ID, 'com.aiosign.dzonesign:id/ivMyShow')

    # 我的套餐按钮
    my_meal_button = (By.ID, 'com.aiosign.dzonesign:id/llMyMeal')

    # 全部文件按钮
    all_file_button = (By.ID, 'com.aiosign.dzonesign:id/tvAllFile')

    # 签署文件按钮
    sign_file_button = (By.ID, 'com.aiosign.dzonesign:id/llSignFile')

    # 待我签按钮
    wait_mine_button = (By.ID, 'com.aiosign.dzonesign:id/flWaitMine')

    # 待他人签按钮
    wait_other_button = (By.ID, 'com.aiosign.dzonesign:id/llWaitOther')

    # 已完成按钮
    has_finish_button = (By.ID, 'com.aiosign.dzonesign:id/llHasFinish')

    def click_personal_center_button(self):
        self.find_element(*self.personal_center_button).click()

    def click_my_meal_button(self):
        self.find_element(*self.my_meal_button).click()

    def click_all_file_button(self):
        self.find_element(*self.all_file_button).click()

    def click_sign_file_button(self):
        self.find_element(*self.sign_file_button).click()

    def click_wait_mine_button(self):
        self.find_element(*self.wait_mine_button).click()

    def click_wait_other_button(self):
        self.find_element(*self.wait_other_button).click()

    def click_has_finish_button(self):
        self.find_element(*self.has_finish_button).click()

    def is_personal_center_button_exist(self):
        return self.is_element_exist(*self.personal_center_button)


if __name__ == '__main__':
    print(123)
