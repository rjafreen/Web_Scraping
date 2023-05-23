# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:17:21 2022

@author: HP
"""


import requests
from bs4 import BeautifulSoup
import time
import smtplib


while True:
   
    url = "https://pastebin.com/Mfc9txQV"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup =  BeautifulSoup(r.text, 'lxml')
    
    if str(soup).find("Key") == -1:
        
        time.sleep(500)
        
        continue
    
    else:
        
        create_email = 'Subject: CHECK PASTEBIN - FOUND KEY'
        from_address = 'from address'
        to_address = 'to address'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        #USE SSL RECOMMENDED
        mail.starttls()
        mail.login("USERNAME", "PW")
        mail.sendmail(from_address, to_address, create_email)
        mail.close()
        print("ALERT")
        
        break
    
    
    
    
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36   