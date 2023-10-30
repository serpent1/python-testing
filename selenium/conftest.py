from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
import uuid
import pytest
'''
不带参数时默认scope="function"

作用范围：scope便是定义用例域的范围

function：默认范围，每一个函数或方法都会调用，不填写时便是它
class：每一个类调用一次
module: 每一个.py文件调用一次，文件中可以有多个function和class
session：多个文件调用一次，可以跨文件，如在.py文件中，每一个.py文件就是module
'''


@pytest.fixture(scope="function")
def launch_broswer():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    path = os.path.dirname(os.path.abspath(__file__))
    file_path = 'file:///' + path + '/index.html'
    driver.get(file_path)
    yield driver
    sleep(3)
    driver.quit()
