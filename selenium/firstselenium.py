import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要

option = Options()                          # オプションを用意
option.add_argument('--incognito')          # シークレットモードの設定を付与
driver = webdriver.Chrome(options=option)   # Chromeを準備(optionでシークレットモードにしている）
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
