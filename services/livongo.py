from instance.config import USERNAME, PASSWORD
from selenium import webdriver
from time import sleep
from datetime import datetime as dt
import dateutil.parser as dparser
from models.user import UserModel
from models.meter import MeterModel
from models.login import LoginModel


class ScrapeLivongo:

    @classmethod
    def scrape(cls, id):
        driver = webdriver.PhantomJS()
        driver.get("https://my.livongo.com")
        cls.login(driver, id)
        cls.navigate(driver)
        cls.scroll(5, driver)
        bgs = driver.find_elements_by_class_name("all-data-bg-value")
        date = driver.find_elements_by_class_name("day-bg")
        time = driver.find_elements_by_class_name("hour-bg")
        cls.save_bgs(bgs, date, time, id)

    @classmethod
    def save_bgs(cls, bgs, date, time, id):
        count = 0
        for b in zip(bgs, date, time):
            bg = b[0].text
            date_str = b[1].text + " " + b[2].text
            date = dparser.parse(date_str)
            print(bg, date, id)
            b = MeterModel(date, bg, id)
            b.save_to_db()
            count += 1
        print(count)

    @classmethod
    def login(cls, driver, id):
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        username.send_keys(LoginModel.find_by_id(id).username)
        password.send_keys(LoginModel.find_by_id(id).password)

    @classmethod
    def navigate(cls, driver):
        driver.find_element_by_class_name('lv-btn').click()
        sleep(3)
        driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[2]/div[1]/nav/div/div[1]/button/img""").click()
        sleep(3)
        driver.find_element_by_xpath("""//*[@id="navbar-collapse-xs"]/ul[1]/li[3]/a/span/span""").click()
        sleep(3)
        driver.find_element_by_xpath(
            """//*[@id="ng-app"]/body/div[2]/div[3]/div[1]/div/div/div[2]/div/div[2]/div/a/img""").click()


    @classmethod
    def scroll(cls, times, driver):
        for i in range(0, times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
