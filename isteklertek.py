 # -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

    
browser.get("https://www.instagram.com/")
time.sleep(2)
girisid = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input""")
girisid.send_keys("--Buraya Kullanıcı Adınızı Giriniz--")
time.sleep(1)
    
    
sifre = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input""")
sifre.send_keys("--Buraya Şifre Giriniz--")
time.sleep(1)
sifre.send_keys(Keys.ENTER)
    
time.sleep(3)
i=1
while i < 250:
    try:
        
        browser.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")    
        time.sleep(4)
        ad = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/main/section/div[1]""").text
        
        print(str(ad))
        browser.get("https://www.instagram.com/"+str(ad))
        
        #//*[@id="react-root"]/section/main/div/header/section/div[2]/button
        time.sleep(3)
        gericek = browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/div[1]/button""")
        time.sleep(1)
        gericek.send_keys(Keys.ENTER)
        time.sleep(2)
        
        #/html/body/div[4]/div/div/div/div[3]/button[1]
        takibibirak =browser.find_element_by_xpath("""/html/body/div[4]/div/div/div/div[3]/button[1]""")
        time.sleep(1)
        takibibirak.send_keys(Keys.ENTER)
        time.sleep(2)
        
        browser.refresh()
        time.sleep(1)
        browser.get("https://www.instagram.com/")
        
        i += 1  
    except:
        print("Silme işlemi tamamlandı")
        i += 250
        browser.close()    
#
