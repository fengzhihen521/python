# coding:utf-8

from selenium import webdriver
from pykeyboard import PyKeyboard #导入键盘操作
from pymouse import PyMouse #导入鼠标操作
import time
import os

driver = webdriver.Firefox()
driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")
time.sleep(3)


os.system("exe可执行文件路径")




# 默认在取消按钮上，先切换到保存文件上
# k = PyKeyboard() #实例化
# s = "文件地址"
# for i in s:
#     k.tab_key(i)
# 发送tab
# k.tab_key(k.enter_key) #回车
# k.press_key(k.tab_key) #按住
# k.release_key(k.tab_key) #放开


# time.sleep(3)
# 发送回车