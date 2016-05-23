#-*- coding:UTF-8 -*-
__author__ = 'andluo'

class Selenium2(object):
    "重新封装Webdriver"

    def __init__(self,webdriver):
        self.driver = webdriver

    def click(self,cssSelector):
        self.driver.find_element_by_css_selector(cssSelector).click()

    def getText(self,cssSelector):
        return self.driver.find_element_by_css_selector(cssSelector).text

    def open(self,url):
        self.driver.get(url)

    def screenshot(self,file):
        self.driver.get_screenshot_as_file(file)