from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome() # 다른경로에 있다면 ("써줘야함")
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem = browser.find_element(By.ID, "query")
# print(elem.click())
# print(browser.back())
# print(browser.forward())
# print(browser.refresh())
# print(browser.back())
# print(elem)
print(elem.send_keys("나도코딩"))
print(elem.send_keys(Keys.ENTER))


elem = browser.find_elements(By.TAG_NAME, "a")

for e in elem:
    print(e.get_attribute("href"))

browser.get("http://daum.net")
elem = browser.find_element(By.NAME, "q")
print(elem)
print(elem.send_keys("나도코딩"))
print(elem.send_keys(Keys.ENTER))
print(browser.back())
elem = browser.find_element(By.NAME, "q")
print(elem.send_keys("나도코딩"))
elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
print(elem)
print(elem.click())
print(browser.quit())

while True:
    pass 