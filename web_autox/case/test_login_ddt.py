
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import time


testdates = [
    {"user":"liuyuepeng","psw":"123456789","expect":"liuyuepeng"},
    {"user":"liuyuepeng","psw":"","expect":""},
    {"user":"liuyuepeng1","psw":"1234567890","expect":""}
]


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
        result = self.loginp.get_login_name()
        print("测试结果:%s"%result)
        self.assertTrue(result == expect)

    #1.输入账号，输入密码，点击登录
    def test_01(self):
        data1 = testdates[0]
        print("测试数据:%s"%data1)
        self.login_case(data1["user"],data1["psw"],data1["expect"])

    #2.输入账号，不输入密码，点击登录
    def test_02(self):
        data2 = testdates[1]
        print("测试数据:%s" % data2)
        self.login_case(data2["user"], data2["psw"], data2["expect"])

    #3.不输入账号，输入密码，点击登录
    def test_03(self):
        data3 = testdates[2]
        print("测试数据:%s" % data3)
        self.login_case(data3["user"], data3["psw"], data3["expect"])


    def tearDown(self):
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()  # 刷新

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()