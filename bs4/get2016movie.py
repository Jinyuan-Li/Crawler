from bs4 import BeautifulSoup
import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

sum_list = []
url0 = 'http://dianying.2345.com/list/----2016---'
url1 = '.html'
for i in range(1, 2, 1):
    url = url0 + str(i) + url1

    dom = requests.get(url, headers = headers)
    # dom.encoding = "utf-8"
    soup = BeautifulSoup(dom.text, 'html.parser')
    aa = soup.find('ul', class_ = 'v_picTxt pic180_240 clearfix')
    bb = aa.find_all('li')

    for i in bb:
        tem_list = []
        if i.find('em'):
            cc = i.find('div', class_='txtPadding')
            tem_list.append(cc.find('em', class_='emTit').get_text())
            dd = cc.find('span', class_='sDes').get_text().replace(u'主演：', '')
            tem_list.append(re.compile(r'\xa0{2,3}').split(dd)[0])
            tem_list.append(re.compile(r'\xa0{2,3}').split(dd)[1])
            tem_list.append("http:" + cc.find('a').get('href'))
            sum_list.append(tem_list)


print(sum_list)
print(len(sum_list))
