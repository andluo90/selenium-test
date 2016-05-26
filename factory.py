#-*- coding:UTF-8 -*-
__author__ = 'andluo'
from selenium import webdriver
from testConfig import TestConfig
from selenium2 import Selenium2

p = TestConfig()

class DeviceFactory:
    '设备工厂'


    @classmethod
    def creatAndroidDev(cls):
        nexus4 = {
        "deviceMetrics": { "width": 384, "height": 640, "pixelRatio": 2 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}
        return nexus4

    @classmethod
    def createIosDev(cls):
        ip5 = {
        "deviceMetrics": { "width": 375, "height": 667, "pixelRatio": 2 },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        return ip5


class WebdriverFactory(object):

    @classmethod
    def createDriver(cls):
        cls.platform = p.get('platform')
        if cls.platform == 'android':
            return cls.createAndroidDriver()
        elif cls.platform == 'ios':
            return cls.createIosDriver()
        elif cls.platform == 'pc':
            return cls.createPcDriver()

    @classmethod
    def createAndroidDriver(cls):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("mobileEmulation",DeviceFactory.creatAndroidDev())
        driver = webdriver.Chrome(executable_path=p.get('driver_path'),chrome_options=chromeOptions)
        return Selenium2(driver)

    @classmethod
    def createIosDriver(cls):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("mobileEmulation",DeviceFactory.createIosDev())
        driver = webdriver.Chrome(executable_path=p.get('driver_path'),chrome_options=chromeOptions)
        return Selenium2(driver)

    @classmethod
    def createPcDriver(cls):
        return Selenium2(webdriver.Chrome(p.get('driver_path')))


