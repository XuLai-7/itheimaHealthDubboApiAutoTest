# 创建 suite 实例
# 添加测试用例
# 创建 HTMLTestReport 类对象
# 调用 run() 传入 suite
import unittest

from htmltestreport import HTMLTestReport

from scripts.test_member_service import TestFindByTelephone

suite = unittest.TestSuite()
# 传入测试脚本的类名, 如果有多个, 就写多行,添加多个测试脚本层的类名
suite.addTest(unittest.makeSuite(TestFindByTelephone))
# suite.addTest(unittest.makeSuite("./scirpt/test*.py"))
runner = HTMLTestReport("./report/传智健康会员服务类测试报告.html",description="会员服务类接口自动化测试",title="传智健康")
runner.run(suite)