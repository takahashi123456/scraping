import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要

option = Options()                          # オプションを用意
option.add_argument('--incognito')          # シークレットモードの設定を付与
driver = webdriver.Chrome(options=option)   # Chromeを準備(optionでシークレットモードにしている）
driver.get('https://books.google.co.jp')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('葬送のフリーレン')
search_box.submit()
time.sleep(3)

i = 1               # ループ番号、ページ番号を定義
i_max = 2           # 最大何ページまで分析するかを定義
title_list = []     # タイトルを格納する空リストを用意
link_list = []      # URLを格納する空リストを用意

while i <= i_max:
    # タイトルとリンクはclass="r"に入っている
    class_group = driver.find_elements_by_class_name('Yr5TG')
        # タイトルとリンクを抽出しリストに追加するforループ
    for elem in class_group:
        title_list.append(elem.find_element_by_class_name('LC20lb').text)           #タイトル(class="LC20lb")
        link_list.append(elem.find_element_by_tag_name('a').get_attribute('href'))  #リンク(aタグのhref属性)
 
        # 「次へ」は1つしかないが、あえてelementsで複数検索。空のリストであれば最終ページの意味になる。
    if driver.find_elements_by_id('pnnext') == []:
        i = i_max + 1
    else:
            # 次ページのURLはid="pnnext"のhref属性
        next_page = driver.find_element_by_id('pnnext').get_attribute('href')
        driver.get(next_page)   # 次ページへ遷移する
        i = i + 1               # iを更新
        time.sleep(3)        



#画像のリンクをクリック
# element.click()

time.sleep(5)
driver.quit()
print(class_group)
print(title_list)
print(len(title_list))
# print(link_list)
