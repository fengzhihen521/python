from selenium import webdriver
import unittest
import time
from pages.login_page import LoginPage
from pages.add_bug_page import AddBugPage

my = "http://210.12.11.100:10082/"

class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = AddBugPage(cls.driver)
        a = LoginPage(cls.driver)
        a.login()

    def setUp(self):
        self.driver.get(my) #打开网址

    #添加bug
    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        titel = "测试bug" + timestr
        self.bug.add_bug(titel)
        result = self.bug.is_add_bug_sucess(titel)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()