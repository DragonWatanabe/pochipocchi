#time.sleep(N)でN秒処理を止めてくれるので、通信環境によって変更する。
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome('./chromedriver.exe')
time.sleep(1)
browser.get('https://scs.cl.sophia.ac.jp/campusweb/campusportal.do')
time.sleep(7)

UserName = browser.find_element(By.NAME,'userName')
UserName.send_keys('A2242114')
PassWord = browser.find_element(By.NAME,'password')
PassWord.send_keys('')
PassWord.submit()
time.sleep(7)

Pulldown1 = browser.find_element(By.XPATH,'//*[@id="tab-rs"]')
Pulldown1.click()

Pulldown2 = browser.find_element(By.XPATH,'//*[@id="tabmenu-li1"]/span')
Pulldown2.click()
time.sleep(3)
Curriculum = browser.find_element(By.XPATH,'//*[@id="tabmenu-sub-ul1"]/li[1]/span')
Curriculum.click()

#Xpathはctrl+shift+Iで検証を開いて、履修登録したい曜日、時限の単位の所のHTMLスクリプトを
# 右クリックし、Copyを押して、Copy Xpathを押せば、Xpathがコピーできている。
Register = browser.find_element(By.XPATH,'曜日、時限のXpathを入力')
for i in range(100000000):
    Register.click()
time.sleep(3000)