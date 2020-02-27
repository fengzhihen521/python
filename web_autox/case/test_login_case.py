
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import time

class LonginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url) #打开网址

    #1.输入账号，输入密码，点击登录
    def test_01(self):
        self.loginp.input_user("liuyuepeng")
        self.loginp.input_psw("123456789")
        self.loginp.click_login_button()

        #断言
        result = self.loginp.get_login_name()
        self.assertTrue(result == "liuyuepeng")

    #2.输入账号，不输入密码，点击登录
    def test_02(self):
        self.loginp.input_user("liuyuepeng")
        self.loginp.click_login_button()

        #断言
        result = self.loginp.get_login_name()
        self.assertTrue(result == "")

    #3.不输入账号，输入密码，点击登录
    def test_03(self):
        self.loginp.input_psw("123456789")
        self.loginp.click_login_button()

        #断言
        result = self.loginp.get_login_name()
        self.assertTrue(result == "")

    # 4.点击忘记密码
    def test_04(self):
        self.loginp.click_forget_psw()
        time.sleep(3)

        # 断言
        result = self.loginp.is_refresh_exist()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()  # 刷新

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()