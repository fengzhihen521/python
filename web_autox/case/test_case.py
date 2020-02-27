# coding:utf-8

from selenium import webdriver
import time
import unittest
from case.login import login

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get("https://sop.linlinyi.cn/manage/toLogin.jhtml?returnurl=http%3A%2F%2Fsop.linlinyi.cn%2F")
        time.sleep(3)

    #判断时候登录成功
    def get_login_username(self):
        try:
            t = self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[1]/div[1]/a/span/span').text
            return t
        except:
            return ""

    #判断是否有alert
    # def is_alert_exist(self):
    #     try:
    #         time.sleep(3)
    #         alert = self.driver.switch_to.alert
    #         text = alert.text
    #         alert.accept() #有alert就点下
    #         return text
    #     except:
    #         return ""

    # def login(self,user,password):
    #     self.driver.find_element_by_name("username").send_keys(user)
    #     self.driver.find_element_by_name("password").send_keys(password)
    #     self.driver.find_element_by_id('loginButton').click()


    def test_01(self):
        '''用例说明3'''
        login(self.driver,"linlinyi","abc123")

        #判断是否登录成功
        time.sleep(3)
        t = self.get_login_username()
        self.assertTrue(t == "您好：linlinyi2")

    def test_02(self):
        '''用例说明4'''
        login(self.driver,"liuyuepeng","abc1234")

        #判断是否登录成功
        time.sleep(3)
        t = self.get_login_username()
        self.assertTrue(t != "您好：linlinyi2") #断言失败

    def tearDown(self):
        # self.is_alert_exist() #判断alert
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()  # 刷新页面

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

        # if t== "liuyuepeng":
        #     print("登录成功")
        # else:
        #     print("登录失败")
        # time.sleep(2)
        #
        # driver.quit()

# if __name__ == "__name__":
#     unittest.main()