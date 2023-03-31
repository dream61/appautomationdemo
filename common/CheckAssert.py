# coding=utf-8
__author__ = '刘影'

from selenium import webdriver
from common.appObject import appObject
from common.ScreenShot import saveScreenShot
from common.log import Log
import HTMLTestRunner
log = Log()

class checkAssert:
    def __init__(self,driver, appObject):
        self.driver = driver
        self.appObject = appObject

    def checkText(self,checkvar, expectvar, *loc, num=None):
        el = self.appObject.testEle(*loc, num=num)
        try:
            if "text" == checkvar:
                s1 = el.text
                if s1 == expectvar:
                    log.info("检查文本，根据对象{0}，与期望值[{1}]一致".format(loc,expectvar))
                else:
                    log.error("检查文本，根据对象{0}，与期望值[{1}]不一致".format(loc,expectvar))
                    raise AssertionError
            else:
                s1 = el.get_attribute(checkvar)
                if s1 == expectvar:
                    log.info("检查文本，根据对象{0}，与期望值[{1}]一致".format(loc,expectvar))
                else:
                    log.error("检查文本，根据对象{0}，与期望值[{1}]不一致".format(loc,expectvar))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("根据对象{0}页面中未能找到{1}元素,检查属性失败".format(loc, screenshotdir))
            raise e

    def checkContainsText(self, checkvar, expectvar, *loc):
        el = self.appObject.testEle(*loc)
        try:
            if "text" == checkvar:
                s1 = el.text
                if s1.Contains(expectvar):
                    log.info("检查包含文本，根据对象{0}，与期望值[{1}]一致".format(loc, expectvar))
                else:
                    log.error("检查包含文本，根据对象{0}，与期望值[{1}]不一致".format(loc, expectvar))
                    raise AssertionError
            else:
                s1 = el.get_attribute(checkvar)
                if s1.Contains(expectvar):
                    log.info("检查包含文本，根据对象{0}，与期望值[{1}]一致".format(loc, expectvar))
                else:
                    log.error("检查包含文本，根据对象{0}，与期望值[{1}]不一致".format(loc, expectvar))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("根据对象{0}页面中未能找到元素,检查属性失败,错误截图{1}".format(loc, screenshotdir))
            raise e

    def checkAttribute(self,checkvar, expectvar, *loc):
        el = self.appObject.testEle(*loc)
        try:
            if checkvar:
                s1 = el.get_attribute(checkvar)
                if s1 == expectvar:
                    log.info("检查文本，根据对象{0}，与期望值[{1}]一致".format(loc,expectvar))
                else:
                    log.error("检查文本，根据对象{0}，与期望值[{1}]不一致".format(loc,expectvar))
                    raise AssertionError
            else:
                s1 = el.get_attribute(checkvar)
                if s1 == expectvar:
                    log.info('预期值与期望值一致')
                else:
                    log.error('预期值与期望值不一致')
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("根据对象{0}页面中未能找到{1}元素,检查属性失败".format(loc, screenshotdir))
            raise e


