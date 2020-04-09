from case.testcase import TestCase
from setting import REPORT_PATG
from tools.HTMLTestRunner import HTMLTestRunner #网上下一个就行
import unittest

# 1.创建测试套件
suite = unittest.TestSuite()
# 2.添加测试用例
suite.addTest(unittest.makeSuite(TestCase))
# 3.指定报告生成位置
with open(REPORT_PATG, "wb") as f:
    runner = HTMLTestRunner(f, title="AsimovApi", description="None")
    runner.run(suite)
