# coding=utf-8
import time
from common.log import Log
from appium import webdriver
from common.ScreenShot import saveScreenShot
from config import setting
log = Log()
class DriverManage():
    def get_driver(self):
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = '127.0.0.1:62001'
            self.desired_caps['appPackage'] = 'tv.danmaku.bili'
            self.desired_caps['appActivity'] = '.MainActivityV2 t3'
            self.desired_caps['unicodeKeyboard'] = True
            self.desired_caps['resetKeyboard'] = True
            self.desired_caps['automationName'] = 'uiautomator2'
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
            return driver
        except Exception as e:
            raise e

