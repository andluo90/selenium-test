#-*- coding:UTF-8 -*-
__author__ = 'Administrator'
import baseTestCase
import unittest
from baseTestCase import  BaseTestCase

class GPTestCase(BaseTestCase):

    @unittest.skip('skip.....')
    def test_addGroup(self):
        "test1"
        s = self.s
        s.open('http://m.guopan.cn/my/userCenter/')
        s.click('.userListaaaa .li0')
        s.click('.myGroupList .add')
        s.click('.Agroup-list li:first .join_btn')
        text = s.getText('.Agroup-list li:first .has')
        self.assertEqual(u'已加入',text)




    def test_33(self):
        pass


if __name__ == '__main__':
    unittest.main()