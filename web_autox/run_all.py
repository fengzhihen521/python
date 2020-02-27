import unittest
from common import HTMLTestRunner_cn #调用HTML报告模块

#用例路径
casePath = "/Users/chabuduoxiansheng/PycharmProjects/web_auto/case"
rule = "test_0*.py"

#查找用例
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)

#print(discover)

#保存报告
reportPath = "/Users/chabuduoxiansheng/PycharmProjects/web_auto/report//"+"result.html"
#打开报告
fp = open(reportPath,"wb")


runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="测试报告",
                                       description="描述报告信息",
                                       retry=1) #失败后重跑
#执行找到的用例
runner.run(discover)

#关闭报告
fp.close()