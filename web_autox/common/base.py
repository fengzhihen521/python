from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By #二次封装
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout=10
        self.t=0.5

    #定位到元素返回元素对象，没定位到发挥Timeout异常
    def findElementNew(self,locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    # 判断定位到元素是否存在
    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型")
        else:
            print("正确定位到元素信息，定位方式—>%s,value值—>%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    #一组元素
    def findElements(self,locator):
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []

    def senKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    #判断元素是否选中
    def isSelected(self,locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    #判断一组元素是否存在
    def isElementExists(self,locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素数：%"%n)
            return False


    #判断元素是否存在
    def isElementExist(self,locator):
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver,3, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            #print("获取text失败，返回''")
            return ""

    def is_title(self,_title):
        '''获取title'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_refresh_exist(self):
        '''判断忘记密码页提交按钮是否存在'''
        r = self.isElementExist(self.loc_forget_psw_page)
        return r

    def is_text_in_element(self,locator,_test=""):
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型")
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return result
        except:
            return False

    #鼠标悬停
    def move_to_elemet(self,locator):
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    #select下拉(index)
    def select_by_index(self,locator,index=0):
        element = self.findElement(locator) #定位select元素
        Select(element).select_by_index(index)

    # select下拉(value)
    def select_by_value(self, locator, value):
        element = self.findElement(locator)  # 定位select元素
        Select(element).select_by_value(value)

    # select下拉(text)
    def select_by_text(self, locator, text):
        element = self.findElement(locator)  # 定位select元素
        Select(element).select_by_visible_text(text)

    #滚动到底部
    def js_scroll_end(self):
        js_heig = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    #横向滚动
    def js_scroll_ends(self,x=0):
        js_heig = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js_heig)

    #聚焦元素
    def js_focus(self,locator):
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    #滚动到顶部
    def js_scroll_top(self):
        js = "window.sctollTo(0,0)"
        self.driver.execute_script(js)




    # def is_alert_exist(self):
    #     '''判断alert是不是存在'''
    #     try:
    #         time.sleep(2)
    #         alert = self.driver.switch_to.alert
    #         text = alert.text
    #         alert.accept() #点击alert
    #         return text
    #     except:
    #         return ""

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://210.12.11.100:10082/login")

    zentao = Base(driver)

    locl = (By.ID, "username")
    #locl = ("name","username")
    locl1 = (By.ID, "password")
    locl2 = (By.ID, "login-submit")

    zentao.senKeys(locl,"liuyuepeng")
    zentao.senKeys(locl1,"123456789")
    zentao.click(locl2)