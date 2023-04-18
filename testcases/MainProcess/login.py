#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/4/18

# 导包
from selenium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

# 创建浏览器驱动对象
driver = webdriver.Chrome()

# 打开百度首页
driver.get("http://192.168.2.236:9527/#/index")

# 浏览器窗口最大化
driver.maximize_window()
sleep(3)

# 点击登录
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "登录").click()

# 休眠2s
sleep(10)

