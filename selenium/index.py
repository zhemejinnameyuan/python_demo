from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
assert "百度一下" in driver.title


searchWord = driver.find_element('id',"kw")
searchWord.clear()
searchWord.send_keys("python selenium")
time.sleep(2)
searchWord.send_keys(Keys.RETURN)
time.sleep(1)
driver.save_screenshot('screenshot.png')











