#-*- coding:UTF-8 -*-
__author__ = 'andluo'

import pickle
from factory import WebdriverFactory
from unittest import  TestCase
from testConfig import TestConfig

class BaseTestCase(TestCase):

    s = WebdriverFactory.createChromeDriver() #driver
    p = TestConfig()


    @classmethod
    def setUpClass(cls):
        "检测是否已登录，如果未登录，则登录后并且保存登录态"

        testUrl = cls.p.get('url')
        user = cls.p.get('user')
        pwd = cls.p.get('pwd')

        cls.s.open(testUrl)

        with open("cookies.pkl","rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            print cookie
            print type(cookie)
            cls.s.addCookie(cookie)

        cls.s.open(testUrl+'/my/userCenter/')

        if cls.s.title == u'登录注册_果盘游戏':
            #登录代码并保存cookie
            cls.s.type("#uname",user)
            cls.s.type("#upwd",pwd)
            cls.s.click(".loginBtn")
            cls.s.sleep(3)
            if cls.s.title == u'个人中心首页_果盘游戏个人中心':
                with open('cookies.pkl','wb') as cookie_file:
                    pickle.dump(cls.s.getCookies(),cookie_file)
            else:
                print 'login fail!'

    @classmethod
    def tearDownClass(cls):
        cls.s.close()
        print('driver closed...')
    def setUp(self):
        pass

    def tearDown(self):
        pass

