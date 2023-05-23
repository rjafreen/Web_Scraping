# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:48:56 2022

@author: HP
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
#time.sleep(5)

def site_login():
    driver.get("https://www.superdatascience.com/login")
    driver.find_element_by_name('email').send_keys("THISISMYEMAIL")
    driver.find_element_by_name('password').send_keys("12345678910")
    driver.find_element_by_xpath('//*[@id="login"]/button').click()
    
site_login()
time.sleep(20)
driver.quit()


    