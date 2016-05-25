#-*- coding:UTF-8 -*-
__author__ = 'andluo'
import time
from testLog import log

class Selenium2(object):
    "重新封装Webdriver"

    def __init__(self,webdriver):
        self.driver = webdriver

    def click(self,cssSelector):
        self.driver.find_element_by_css_selector(cssSelector).click()
        log.info("click "+cssSelector)

    def type(self,cssSelector,content):
        self.driver.find_element_by_css_selector(cssSelector).send_keys(content)
        log.info("type "+cssSelector)

    def getText(self,cssSelector):
        text = self.driver.find_element_by_css_selector(cssSelector).text
        log.info("getText "+text)
        return text

    def open(self,url):
        self.driver.get(url)
        log.info("open "+url)

    def screenshot(self,file):
        self.driver.get_screenshot_as_file('./screenshot/'+file)
        log.info("screenshot "+file)

    def sleep(self,second):
        time.sleep(second)

    def getCookies(self):
        return self.driver.get_cookies()

    def addCookie(self,cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def close(self):
        self.driver.close()
        log.info("driver close.")

    @property
    def title(self):
        title = self.driver.title.encode('UTF-8')
        log.info("title "+title)
        return title

