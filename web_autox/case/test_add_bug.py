import time
import unittest

from selenium import webdriver

from pages.add_bug_page import ZenTaoBug


class Test_Add_Bug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        titel = "测试bug"+timestr
        self.bug.add_bug(titel)
        result = self.bug.is_add_bug_sucess(titel)
        print(result)
        self.assertTrue(result)# 断言

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()