#-*- coding:UTF-8 -*-
__author__ = 'Administrator'
import ConfigParser


class TestConfig(object):
    "Test config"
    def __init__(self,file='./config/test.conf'):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(file)
        self.baseSection = 'test-config'

    def get(self,option):
        return self.cf.get(self.baseSection,option)

