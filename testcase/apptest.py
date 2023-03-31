#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ASUS
# datetime:2023/3/28 17:01
# software: PyCharm

from appium import webdriver

desired_caps ={
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "tv.danmaku.bili",
    "appActivity": ".MainActivityV2 t3",
    "unicodeKeyBoard": True,
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element('id', 'tv.danmaku.bili:id/agree').click()
driver.implicitly_wait(300)
driver.find_element('id','tv.danmaku.bili:id/search_src_text').send_keys('english')
#driver.find_element('class_name','android.widget.ImageView').click()
