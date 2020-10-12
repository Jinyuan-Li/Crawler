import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

page = 2 # 1頁15篇
sum_list = [['url', 'key_word', 'title', 'date']]
url_list = []

def get_list():
    key_word = ["自殺", "輕生", "燒炭", "上吊"]
    for i in key_word:
        for p in range(1, page + 1):
            # if i == "自殺":
                dom = requests.get("https://news.ltn.com.tw/search?keyword=" + i + "&page=" + str(p))
                soup = BeautifulSoup(dom.text, 'html.parser')
                list = soup.find("ul", class_="searchlist boxTitle")
                try:
                    for title, date in zip(list.find_all("a", class_="tit"), list.find_all("span")):
                        url = title.get("href")
                        if url not in url_list:
                            tem_list = []
                            url_list.append(url)
                            tem_list.append(url)
                            tem_list.append(i)
                            tem_list.append(title.text)
                            tem_list.append(date.text.split(" ")[0])
                            sum_list.append(tem_list)
                        else:
                            for k in range(len(sum_list)):
                                if url == sum_list[k][0]:
                                    sum_list[k][1] += "、" + i
                except:
                    z = 0
    df = pd.DataFrame(sum_list)
    df.to_excel(r'C:\Users\user\Desktop\ltn.xlsx', sheet_name='ltn', index=0, header=0)
    print(len(sum_list))

get_list()

