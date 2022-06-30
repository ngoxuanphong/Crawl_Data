import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium.webdriver.chrome.options import Options


class setup():
    
    def __init__(self):
        self.amount = 0
        self.driver = None
        self.path='C:\webdrive\Driver\chromedriver.exe'
        # self.path="C:/webdrive/msedgedriver.exe"
        self.proxyList = [
           '14.225.7.148:8081',
           "90.181.150.210:4145",
           '27.72.73.143:4153',
           '103.74.121.46:35612',
           '123.25.15.209:9812',
           '116.110.18.247:1080',
           '113.176.195.145:4153'
        ]
        pass

    def reset_driver(self):

        # t = random.choice(self.proxyList)
        # self.proxyList.remove(t)
        # print(t, self.proxyList)
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument('--proxy-server={}'.format(t))
        self.driver = webdriver.Chrome(executable_path=self.path)
        # self.driver = webdriver.ChromiumEdge(executable_path=self.path)
        self.driver.get("https://www.onlineocr.net")
        

    def push_something_by_id(self, something, path):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, something))
            )
            element.send_keys(path)
        except:
            self.driver.close()
            self.reset_driver()


    def click_something_by_id(self, something):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, something))
            )

            # print(element)
            self.driver.execute_script("arguments[0].click();", element)
        except:
            self.driver.close()
            self.reset_driver()
    
    def click_something_by_xpath(self, something):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, something))
            )

            # print(element)
            self.driver.execute_script("arguments[0].click();", element)
        except:
            self.driver.close()
            self.reset_driver()

    def select(self):
        select = Select(self.driver.find_element_by_name(
            'ctl00$MainContent$comboOutput'))
        select.select_by_value("Microsoft Excel (xlsx)")

    def get(self,path_image):
        if self.amount%10 == 0:
            self.reset_driver()
        self.push_something_by_id("fileupload", path_image)
        time.sleep(5)
        self.select()
        self.click_something_by_id("MainContent_btnOCRConvert")
        time.sleep(10)
        self.click_something_by_xpath('//*[@id="MainContent_lnkBtnDownloadOutput"]')
        # print("xuli!!!done")
        # print(self.amount)
        self.amount+=1