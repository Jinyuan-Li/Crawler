import pandas as pd
from selenium import webdriver
from datetime import timedelta, datetime

n_per_key = 10 # 各關鍵字找幾篇新聞
sum_list = [['date', 'meida_name', 'key_word', 'title', 'url']]
url_list = []
dt = datetime.today() - timedelta(7)

def get_list():
    key_word = ["自殺", "輕生", "燒炭", "上吊"]
    driver = webdriver.Chrome(executable_path=r"D:\JetBrains\chromedriver")
    for i in key_word:
        # if i == "自殺":
            driver.get("https://udn.com/search/word/2/" + i)
            for n in range(1, n_per_key + 1):
                mid = "section/div[" + str(n-20) if n > 20 else "div[" + str(n)
                try:
                    date = driver.find_element_by_xpath('/html/body/main/div/section[2]/section/div[2]/' + mid + ']/div[2]/div/time').text.split(" ")[0]
                    if date > dt.strftime('%Y-%m-%d'):
                        url = driver.find_element_by_xpath('/html/body/main/div/section[2]/section/div[2]/' + mid + ']/div[2]/h2/a').get_attribute("href")
                        if url not in url_list:
                            tem_list = []
                            url_list.append(url)
                            tem_list.append(date)
                            tem_list.append("聯合報")
                            tem_list.append(i)
                            tem_list.append(driver.find_element_by_xpath('/html/body/main/div/section[2]/section/div[2]/' + mid + ']/div[2]/h2/a').text.replace('\u3000', ' '))
                            tem_list.append(url)
                            sum_list.append(tem_list)
                            driver.execute_script('window.scrollBy(0,500)')
                        else:
                            for k in range(len(sum_list)):
                                if url == sum_list[k][4]:
                                    sum_list[k][2] += "、" + i
                    else:
                        break
                except:
                    z = 0
    driver.quit()
    df = pd.DataFrame(sum_list)
    df.to_excel(r'C:\Users\user\Desktop\udn.xlsx', sheet_name='udn', index=0, header=0)
    print(len(sum_list))

get_list()

