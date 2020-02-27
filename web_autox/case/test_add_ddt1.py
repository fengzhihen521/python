import os
import unittest

import ddt
from selenium import webdriver

from common.read_excel import ExcelUtil
from pages.login_page import LoginPage, login_url

# testdates = [
#     {"user":"liuyuepeng","psw":"123456789","expect":True},
#     {"user":"liuyuepeng","psw":"","expect":False},
#     {"user":"liuyuepeng1","psw":"1234567890","expect":False}
# ]

curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#项目相关路径
filepath = os.path.join(curpath,"common","ceshishuju.xlsx")#用项目相关路径+文件路径
#print(filepath) #打印路径

# filepath = r"/Users/chabuduoxiansheng/PycharmProjects/练习/API/common/ceshishuju.xlsx"
data = ExcelUtil(filepath)
testdates = data.dict_data()
#print(testdates) 打印数据

@ddt.ddt #增加ddt
class LonginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url) #打开网址

    def login_case(self,user,psw,expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        #断言
        #result = self.loginp.get_login_name()# 判断元素是否存在
        result = self.loginp.get_login_result(user) # 判断元素文本是否正确
        if expect == "True":expect_result = True
        else:expect_result = False
        print("测试结果:%s"%result)
        self.assertTrue(result == expect)

    @ddt.data(*testdates) #传testdates中的参数
    #1.输入账号，输入密码，点击登录
    def test_01(self,data):
        #data1 = testdates[0]
        print("测试数据:%s"%data)
        self.login_case(data["user"],data["psw"],data["expect"])

    def tearDown(self):
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()  # 刷新

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()