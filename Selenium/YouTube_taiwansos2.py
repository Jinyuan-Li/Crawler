import time
import pandas as pd
from selenium import webdriver
t0 = time.time()

driver = webdriver.Chrome(executable_path=r"D:\JetBrains\chromedriver")

sum_list = [['playlist_title','video_title']]
def get_href(): #取出各頁面各列詳細資料中網址
    driver.get('https://www.youtube.com/user/taiwansos/playlists')

    for i in range(20):
        # if i < 100:
            try:
                driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-playlist-renderer[' + str(i + 1) + ']/yt-formatted-string/a').click()
                time.sleep(3)
                # aa = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/h1/yt-formatted-string/a').text
                for j in range(999):
                    try:
                        tem_list = []
                        tem_list.append(driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/h1/yt-formatted-string/a').text)
                        tem_list.append(driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[' + str(j + 1) + ']/div/a/div/h3/span').text)
                        sum_list.append(tem_list)
                    except:
                        break
                driver.back()
                # driver.implicitly_wait(5)
            except:
                break
    driver.quit()
    # print(sum_list)
    df = pd.DataFrame(sum_list)
    df.to_excel(r'C:\Users\user\Desktop\YouTube_playlists.xlsx', sheet_name='playlists', index=0, header=0)


get_href()
print('花費時間：',time.time()-t0)