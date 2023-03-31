# coding=utf-8
__author__ = '刘影'

from appium import webdriver
from common.appObject import appObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from common.ScreenShot import saveScreenShot
from common.log import Log
import os

log = Log()
class commonOperate():
    def __init__(self,driver, appObject):
        self.driver = driver
        self.appObject = appObject


#单击元素
    #num:如操作一组元素中的一个，num为传整数
    def click(self, *loc, num=None):
        el = self.appObject.testEle(*loc, num=num)
        try:
            el.click()
            log.info("单击，根据对象{0}，操作成功".format(loc))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("单击，根据对象,单击失败,错误截图请见：{0}".format(screenshotdir))
            raise e

    def sendKeys(self, value, *loc, num=None):
        el = self.appObject.testEle(*loc, num=num)
        try:
            el.clear()
            el.send_keys(value)
            log.info("输入，根据对象{0},输入{1}成功".format(loc, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("输入，根据对象,输入失败,错误截图请见：{0}".format(screenshotdir))
            raise e


#获取元素属性值
    def get_attribute(self, provalue, *loc, num=None):
        el = self.appObject.testEle(*loc, num=num)
        try:
            s1=el.getAttribute(provalue)
            log.info("获取元素属性值，根据对象{0},获取{1}成功".format(loc, provalue))
            return s1
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("输入，根据对象,输入失败,错误截图请见：{0}".format(screenshotdir))
            raise e



#根据坐标移动
    def moveXY(self,x,y,*loc, num=None):
        el = self.appObject.testEle(*loc, num=num)
        try:
            touch_action = TouchAction(self.driver)
            touch_action.move_to(*loc, x, y)
            log.info("根据坐标移动，根据对象{0},移动{1},{y}成功".format(loc,x,y))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("根据坐标移动，根据对象{0},移动失败,错误截图请见：{1}".format(loc,screenshotdir))
            raise e

#从一个元素移到另一元素位置
    def emementScroll(self,os,el):
        try:
            self.driver.scroll(os, el)
            log.info("根据元素移动成功")
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("根据元素移动失败,错误截图{0}".format(screenshotdir))
            raise e








