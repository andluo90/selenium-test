#-*- coding:UTF-8 -*-
__author__ = 'andluo'
from selenium import webdriver
from testConfig import TestConfig

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
        pass


class WebdriverFactory:

    @classmethod
    def createChromeDriver(cls):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("mobileEmulation",DeviceFactory.creatAndroidDev())
        driver = webdriver.Chrome(executable_path=p.get('driver_path'),chrome_options=chromeOptions)
        return driver