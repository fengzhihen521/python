#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from selenium.webdriver.support.ui import Select

class AddBugPage(Base): #继承Base

    #添加BUG
    loc_test = ("link text","项目")
    loc_bug = ("link text","001仓库")
    loc_question = ("xpath", "//*[@id='main-menu']/ul/li[4]/a")
    loc_question_new = ("link text", "新建问题")
    loc_input_title = ("id","issue_subject")
    loc_input_body = ("id", "issue_description")
    loc_tijiao_button = ("xpath","//*[@id='issue-form']/input[3]")

    #判断
    loc_new = ("xpath","//*[@id='flash_notice']/text()[2]")

    def add_bug(self,title="测试bug"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_question)
        self.click(self.loc_question_new)

        self.senKeys(self.loc_input_title,title)

        body = '''第一步：XXX
        第二步：yyy
        结果：bbb
        '''
        self.senKeys(self.loc_input_body,body)
        loc_truck = self.driver.find_element_by_xpath("//*[@id='issue_assigned_to_id']").click()
        driver.find_element_by_xpath("//*[@id='issue_assigned_to_id']/option[5]").click()
        # Select(loc_truck).select_by_visible_text("刘 悦鹏")
        # loc_truck.click()
        self.click(self.loc_tijiao_button)
        time.sleep(3)

    def is_add_bug_sucess(self,_text):
        return self.is_text_in_element(self.loc_new,_text)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    bug = AddBugPage(driver)

    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    titel = "测试bug"+timestr
    bug.add_bug(titel)
    result = bug.is_add_bug_sucess(titel)
    print(result)