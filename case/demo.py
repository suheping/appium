# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2020/03/06 15:00:05
@Author  :   peace_su
@Version :   1.0
@Contact :   peace_su@163.com
@WebSite :   https://me.csdn.net/u010098760
'''

# here put the import lib
from appium import webdriver
import time

# apk参数
desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',  # 手机设备名称，通过adb devices查看
    'platformVersion': '5.1.1',  # android系统的版本号
    'appPackage': 'com.aiosign.dzonesign',  # apk包名
    # apk的launcherActivity
    'appActivity': 'com.aiosign.dzonesign.view.AppStartActivity',
}
# 启动app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
# 我的app启动后是欢迎页，需要滑动
# 获取屏幕尺寸
sizes = driver.get_window_size()
# 滑动
driver.swipe(sizes.get('width')*0.9, sizes.get('height')*0.5, sizes.get('width')*0.2, sizes.get('height')*0.5)
