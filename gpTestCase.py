#-*- coding:UTF-8 -*-
__author__ = 'Administrator'
import baseTestCase
import unittest
from selenium.common.exceptions import WebDriverException
from baseTestCase import  BaseTestCase

class GPTestCase(BaseTestCase):

    @unittest.skip('test')
    def test_addGroup(self):
        "test1"
        try:
            self.driver.get('http://m.guopan.cn/my/userCenter/')
            self.driver.find_element_by_css_selector('.userList .li0').click()
            #self.driver.find_element_by_css_selector('abcdef').click()
            self.driver.find_element_by_css_selector('.myGroupList .add').click()
            self.driver.find_element_by_css_selector('.Agroup-list li:first .join_btn').click()
            text = self.driver.find_element_by_css_selector('.Agroup-list li:first .has').text
            if text != u'已加入':
                pass
        except WebDriverException,e:
            raise WebDriverException(msg=e.msg,screen=self.driver.get_screenshot_as_file('./test.png'))

    @unittest.skip('test')
    def test_addGroup2(self):
        "test2"
        self.driver.get('http://m.guopan.cn/my/userCenter/')
        self.driver.find_element_by_css_selector('.userList .li0').click()
        #self.driver.find_element_by_css_selector('abcdef').click()
        self.driver.find_element_by_css_selector('.myGroupList .add').click()
        self.driver.find_element_by_css_selector('.Agroup-list li:first .join_btn').click()
        text = self.driver.find_element_by_css_selector('.Agroup-list li:first .has').text
        if text != u'已加入':
            pass

    def test_33(self):
        self.fail('test fail...')

    def test_44(self):
        pass

    def test_55(self):
        pass

if __name__ == '__main__':
    unittest.main()