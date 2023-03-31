# coding=utf-8
__author__ = '刘影'

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from common.ScreenShot import saveScreenShot
from common.log import Log

log = Log()
class touchOperate():
    def __init__(self,driver):
        self.driver = driver


#启动应用程序
    def start_activity(self, appName, appActiity):
        try:
            self.driver.start_activity(appName, appActiity)
            log.info("启动应用程序成功")
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("启动应用程序失败,错误截图{0}".format(screenshotdir))

        # 安装应用程序
    def installApp(self, path):
        try:
            self.driver.install_app(path)
            log.info("安装应用程序成功")
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("安装应用程序失败,错误截图{0}".format(screenshotdir))
            raise e


#手指滑操作
    def add_tysor_swipe(self, n):
        try:
            # 下滑操作，（下滑操作时sx不变，变得的是sy，ey）
            x = self.driver.get_window_size()["width"]
            y = self.driver.get_window_size()["height"]
            sx = x * 0.05
            sy = y * 0.78
            ey = y * 0.73
            for i in range(n):
                self.driver.swipe(sx, sy, sx, ey)
            log.info("下滑操作成功")
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("下滑操作失败,错误截图{0}".format(screenshotdir))
            raise e










