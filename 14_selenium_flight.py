import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일, 28일 선택
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button/b").click()
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button/b").click()

# 다음달 27일, 28일 선택
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[1]/button/b").click()
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/button/b").click()

# 이번달 27일, 다음달 28일 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button/b").click()
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/button/b").click()

# 도착지 선택
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[2]/span/i[1]").click()

# 항공권 검색 클릭
time.sleep(1)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]")))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div/button")
# print(elem.text)


while True:
    pass