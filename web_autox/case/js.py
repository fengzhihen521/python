from selenium import webdriver
from pages.login_page import LoginPage
driver = webdriver.Chrome()
a = LoginPage(driver)
a.login()


#js定位切换iframe
js = 'document.getElementsByClassName("定位")[0]\.contentWindow.document.body.innerHTML="内容"'
driver.execute_script(js)

#js定位切换iframe
body = "参数化"
js = 'document.getElementsByClassName("定位")[0]\.contentWindow.document.body.innerHTML="%s"'%body
driver.execute_script(js)

#js定位输入和点击
js = 'document.getElementById("定位").value="输入内容":'
js = 'document.getElementsByName("定位")[0].value="输入内容":'
js = 'document.getElementById("定位").click():'
driver.execute_script(js)

#js定位日历控件readonly
js = 'document.getElementById("定位").removeAttribute("readonly")' #removeAttribute 删除属性
js1 = 'document.getElementById("定位").value="输入内容":'
driver.execute_script(js1)

#js定位日历控件多行写成一行使用；号和'''内容'''
js = '''document.getElementById("定位").removeAttribute("readonly")';
document.getElementById("定位").value="输入内容"'''
driver.execute_script(js)

#js控制纵向滚动条位置（内嵌滚动条）
js = 'document.getElementsByClassName("定位")[0].scrollTop=10000'
driver.execute_script(js)

#js控制横向滚动条位置（内嵌滚动条）
js = 'document.getElementsByClassName("定位")[0].scrollLeft=10000'
driver.execute_script(js)

#js直接点击
js = 'document.getElementsByClassName("定位")[0].clikc();'
driver.execute_script(js)



