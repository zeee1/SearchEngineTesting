from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

testURL = "https://www.naver.com"
searchKeyword = "keyword"

# test on firefox using explicit wait
result = 0
driver = webdriver.Chrome()

for i in range(1,10):
	driver.implicitly_wait(3)
	driver.get(testURL)
	inputElem = driver.find_element_by_id('query')
	inputElem.send_keys(searchKeyword)
	inputElem.send_keys(Keys.RETURN)

	submitStartTime = time.time()

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
	renderEndTime = time.time()

	responseTime = renderEndTime - submitStartTime
	result += responseTime
	time.sleep(random.randint(1,5))

result = result/10
print(result)

# Compare rendering time between domestic web service and abroad web service
urlList = ["http://www.naver.com", "http://www.daum.net", "http://www.baidu.com", "http://www.google.com", "http://www.yahoo.com"]

