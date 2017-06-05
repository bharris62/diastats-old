from instance.config import USERNAME, PASSWORD
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

CHROME_PATH = "C:\\Users\\abbh62\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.PhantomJS()
driver.get("https://my.livongo.com")
driver.save_screenshot("test1.jpg")
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
driver.save_screenshot("test2.jpg")
button = driver.find_element_by_class_name('lv-btn').click()
sleep(3)
driver.save_screenshot("test3.jpg")
driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[2]/div[1]/nav/div/div[1]/button/img""").click()
sleep(3)
driver.save_screenshot("test4.jpg")
driver.find_element_by_xpath("""//*[@id="navbar-collapse-xs"]/ul[1]/li[3]/a/span/span""").click()
sleep(3)
driver.save_screenshot("test5.jpg")
driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[2]/div[3]/div[1]/div/div/div[2]/div/div[2]/div/a/img""").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
bgs = driver.find_elements_by_class_name("all-data-bg-value")
date = driver.find_elements_by_class_name("day-bg")
time = driver.find_elements_by_class_name("hour-bg")
count = 0
for b in bgs:
    print(b.text)
    count +=1
print(count)
driver.save_screenshot("test6.jpg")
