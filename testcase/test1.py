#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ASUS
# datetime:2023/3/29 17:11
# software: PyCharm

import time
import unittest
from common.readYamlData import getYamlData
from common.commonOperate import commonOperate
from common.DriverManage import DriverManage
from common.appObject import appObject
from common.CheckAssert import checkAssert
from common.touchOperate import touchOperate
from config import setting


class TestLong(unittest.TestCase):
    driver = DriverManage()
    edata = setting.TEST_Element_YAML + "/" + "testapp.yaml"

    def setUp(self):
        self.driver = DriverManage().get_driver()
        self.wb = appObject(self.driver)
        self.to = touchOperate(self.driver)
        self.cn = commonOperate(self.driver, self.wb)
        self.ck = checkAssert(self.driver, self.wb)

    def test_long_1(self):
        self.cn.click(getYamlData(self.edata)['element'][0]['find_type'],
                      getYamlData(self.edata)['element'][0]['element_info'])
        self.driver.implicitly_wait(15000)
        self.ck.checkText(getYamlData(self.edata)['element'][2]['info'],
                          getYamlData(self.edata)['element'][2]['expvalue'],
                          getYamlData(self.edata)['element'][2]['find_type'],
                          getYamlData(self.edata)['element'][2]['element_info'],
                          num=1
                          )
        self.cn.click(getYamlData(self.edata)['element'][1]['find_type'],
                      getYamlData(self.edata)['element'][1]['element_info'])
        self.cn.sendKeys(getYamlData(self.edata)['element'][3]['info'],
                         getYamlData(self.edata)['element'][3]['find_type'],
                         getYamlData(self.edata)['element'][3]['element_info']
                         )
        self.driver.press_keycode(66)
        self.driver.implicitly_wait(5000)
        self.ck.checkText(getYamlData(self.edata)['element'][2]['info'],
                          "综合",
                          getYamlData(self.edata)['element'][2]['find_type'],
                          getYamlData(self.edata)['element'][2]['element_info'],
                          num=0
                          )
        self.to.add_tysor_swipe(10)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()