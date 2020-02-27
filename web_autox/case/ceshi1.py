#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from selenium.webdriver.support.ui import Select

class ZenTaoBug(Base): #继承Base
    #定位登录
    locl1 = ("id", "username")
    locl2 = ("id", "password")
    locl3 = ("id", "login-submit")

    #添加BUG
    loc_test = ("link text","项目")
    loc_bug = ("link text","001仓库")
    loc_question = ("xpath", "//*[@id='main-menu']/ul/li[4]/a")
    loc_question_new = ("link text", "新建问题")
    loc_input_title = ("id","issue_subject")
    loc_input_body = ("id", "issue_description")
    loc_tijiao_button = ("xpath","//*[@id='issue-form']/input[3]")


    def login(self,user="liuyuepeng",psw="123456789"):
        self.driver.get("http://210.12.11.100:10082/login")
        time.sleep(2)
        self.senKeys(self.locl1,user)
        self.senKeys(self.locl2,psw)
        self.click(self.locl3)

    def add_bug(self):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_question)
        self.click(self.loc_question_new)
        self.senKeys(self.loc_input_title,"测试title")
        self.click(self.loc_input_body)
        self.senKeys(self.loc_input_body,"测试body")
        time.sleep(3)
        loc_truck = self.driver.find_element_by_xpath("//*[@id='issue_assigned_to_id']")
        Select(loc_truck).select_by_visible_text("刘 悦鹏")
        #Select(loc_truck).select_by_index(5)
        loc_truck.click()
        self.click(self.loc_tijiao_button)
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    bug = ZenTaoBug(driver)
    bug.login()
    bug.add_bug()