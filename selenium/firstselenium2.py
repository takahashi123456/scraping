import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要

textlist = []

option = Options()                          # オプションを用意
option.add_argument('--incognito')          # シークレットモードの設定を付与
driver = webdriver.Chrome(options=option)   # Chromeを準備(optionでシークレットモードにしている）
driver.get('https://books.google.co.jp')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('葬送のフリーレン')
search_box.submit()
time.sleep(3)
class_group = driver.find_elements_by_class_name('r')
element = driver.find_element_by_class_name("LC20lb")
textlist.append(driver.find_element_by_class_name('LC20lb').text)
#画像のリンクをクリック
element.click()

time.sleep(5)
driver.quit()
print(class_group)
print(textlist)