#coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url = "http://210.12.11.100:10082/login"

class LoginPage(Base): #继承Base
    #定位登录
    loc_user = ("id", "username")
    loc_psw = ("id", "password")
    loc_button = ("id", "login-submit")
    loc_forget_psw = ("xpath","//*[@id='login-form']/form/label[2]/a")

    #登录成功文本
    loc_get_user = ("xpath","//*[@id='loggedas']/a")
    loc_forget_psw_page = ("xpath","//*[@id='content']/form/div/p/input[2]")

    def input_user(self,text=""):
        self.senKeys(self.loc_user,text)

    def input_psw(self, text=""):
        self.senKeys(self.loc_psw,text)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)

    #判断时候登录成功
    def get_login_name(self):
        user = self.get_text(self.loc_get_user)
        return user

    #判断时候登录成功-元素文本
    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_user,user)
        return result

    def is_alert_exist(self):
        '''判断alert是不是存在'''
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()

    #登录                                             #增加一个开关
    def login(self,user="liuyuepeng",psw="123456789",keep_login=False):
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if keep_login:self.click.keep_login()
        self.click_login_button()


if __name__ == "__main__":
    driver = webdriver.Chrome() #打开浏览器
    driver.get(login_url) #打开页面
    login_page = LoginPage(driver)
    login_page.login(keep_login=True)#等于True就点击,默认为False
    time.sleep(3)
    driver.quit()

    # def login(self,user="liuyuepeng",psw="123456789"):
    #     self.driver.get("http://210.12.11.100:10082/login")
    #     time.sleep(2)
    #     self.senKeys(self.locl1,user)
    #     self.senKeys(self.locl2,psw)
    #     self.click(self.locl3)