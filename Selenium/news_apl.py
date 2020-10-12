import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

n_per_key = 30 # 各關鍵字找幾篇新聞 每多20篇需按頁面底部'顯示更多結果'按鍵
sum_list = [['url', 'key_word', 'title', 'date']]
url_list = []

def get_list():
    key_word = ["自殺", "輕生", "燒炭", "上吊"]
    driver = webdriver.Chrome(executable_path=r"D:\JetBrains\chromedriver")
    for i in key_word:
        # if i == "自殺":
            driver.get("https://tw.appledaily.com/search/result?querystrS=" + i)
            for n in range(1, n_per_key + 1):
                try:
                    if n > 10 and n % 20 == 1:
                        driver.find_element_by_xpath('//*[@id="moreButton"]').click()
                    url = driver.find_element_by_xpath('//*[@id="result"]/li[' + str(n) + ']/div/h2/a').get_attribute("href")
                    if url not in url_list:
                        tem_list = []
                        url_list.append(url)
                        tem_list.append(url)
                        tem_list.append(i)
                        tem_list.append(driver.find_element_by_xpath('//*[@id="result"]/li[' + str(n) + ']/div/h2/a').text)
                        tem_list.append(driver.find_element_by_xpath('//*[@id="result"]/li[' + str(n) + ']/div/time').text)
                        sum_list.append(tem_list)
                        driver.execute_script('window.scrollBy(0,155.1)')
                        # driver.execute_script('window.scrollBy(0,300)')
                    else:
                        for k in range(len(sum_list)):
                            if url == sum_list[k][0]:
                                sum_list[k][1] += "、" + i
                except:
                    z = 0
    driver.quit()
    df = pd.DataFrame(sum_list)
    df.to_excel(r'C:\Users\user\Desktop\apl.xlsx', sheet_name='apl', index=0, header=0)
    print(len(sum_list))

get_list()