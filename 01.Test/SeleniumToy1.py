
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# pip install selenium <--설치함
# pip install webdriver_manager <--설치함

#드라이버
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#검색 키워드
keyword = '조경수'

#google로  접속해봄
driver.get("https://google.com")
search1 = driver.find_element(By.NAME, 'q')
print(search1)

search1.send_keys(keyword)
#3초대기
time.sleep(3)
search1.submit()

time.sleep(3)

#스크린샷
driver.save_screenshot('./img/search1_'+keyword+'.png')

#3초대기
time.sleep(3)


#5초대기
time.sleep(3)

#종료
driver.quit()

