#-*- coding:UTF-8 -*-
__author__ = 'andluo'

import pickle
from factory import WebdriverFactory
from unittest import  TestCase
from testConfig import TestConfig
from testLog import  log
import sys

class BaseTestCase(TestCase):

    s = WebdriverFactory.createDriver() #driver
    p = TestConfig()


    @classmethod
    def setUpClass(cls):
        "open the testUrl"
        testUrl = cls.p.get('url')
        user = cls.p.get('user')
        pwd = cls.p.get('pwd')

        cls.s.open(testUrl)


    @classmethod
    def tearDownClass(cls):
        cls.s.quit()

    def setUp(self):
        log.info(">>>>>>start "+self._testMethodName+" <<<<<<")

    def tearDown(self):
        if sys.exc_info()[0]:
            log.error(sys.exc_info()[1])
            self.s.screenshot(self._testMethodName+'.png')
        log.info(">>>>>>end "+self._testMethodName+" <<<<<<")

