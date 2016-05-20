#-*- coding:UTF-8 -*-
__author__ = 'Administrator'

import unittest
import HTMLTestRunner
from gpTestCase import GPTestCase

# get the directory path to output report file
dir = './report'

#config
tests = unittest.TestLoader().loadTestsFromTestCase(GPTestCase)

# create a test suite
smoke_tests = unittest.TestSuite([tests])

# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=outfile,
                 title='Test Report',
                 description='Smoke Tests'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)