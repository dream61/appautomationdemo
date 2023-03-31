# coding=utf-8
__author__ = '刘影'

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.ScreenShot import saveScreenShot
from common.log import Log

log = Log()
class appObject():

    def __init__(self, driver):
        self.driver = driver

    # 定位查找元素
    def testEle(self, *loc, num=None):
        if num is not None:
            try:
                WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
                el = self.driver.find_elements(*loc)[num]
            except Exception as e:
                screenshotdir = saveScreenShot(self.driver)
                log.error("定位元素，根据对象定位失败,错误截图请见：{0}".format(screenshotdir))
                raise e
        else:
            el = self.driver.find_element(*loc)
            log.info('定位元素成功')
        return el

    # 定位一组元素
    def findElements(self, *loc):
        el = self.driver.find_elements(*loc)
        return el
