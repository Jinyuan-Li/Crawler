from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

sum_list = []
url0 = 'https://www.qidian.com/all?action=1&page='
url1 = '&style=1&pageSize=20&siteid=1'
for i in range(1, 3, 1):
    url = url0 + str(i) + url1

    dom = requests.get(url, headers = headers)
    dom.encoding = "utf-8"
    soup = BeautifulSoup(dom.text, 'html.parser')
    aa = soup.find('ul', class_ = 'all-img-list cf')
    bb = aa.find_all('li')


    for i in bb:
        tem_list = []
        tem_list.append(i.find('h4').get_text())
        tem_list.append(i.find('a', class_ = 'name').get_text())
        cc = i.find('p', class_ = 'author')
        tem_list.append(cc.find_all('a')[1].get_text())
        tem_list.append(i.find('a', class_ = 'go-sub-type').get_text())
        tem_list.append(i.find('span').get_text())
        tem_list.append(i.find('p', class_='intro').get_text().strip())
        sum_list.append(tem_list)


print(sum_list)
print(len(sum_list))
