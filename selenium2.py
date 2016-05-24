#-*- coding:UTF-8 -*-
__author__ = 'andluo'
import time

class Selenium2(object):
    "重新封装Webdriver"

    def __init__(self,webdriver):
        self.driver = webdriver

    def click(self,cssSelector):
        self.driver.find_element_by_css_selector(cssSelector).click()

    def type(self,cssSelector,content):
        self.driver.find_element_by_css_selector(cssSelector).send_keys(content)

    def getText(self,cssSelector):
        return self.driver.find_element_by_css_selector(cssSelector).text

    def open(self,url):
        self.driver.get(url)

    def screenshot(self,file):
        self.driver.get_screenshot_as_file(file)

    def sleep(self,second):
        time.sleep(second)

    def getCookies(self):
        return self.driver.get_cookies()

    def addCookie(self,cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def close(self):
        self.driver.close()

    @property
    def title(self):
        return self.driver.title

