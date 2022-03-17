from selenium import webdriver
from selenium.webdriver import ChromeOptions
from common.browserOperator import BrowserOperator


class getDriver:
    def __init__(self):
        option = ChromeOptions()
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('http://www.swu.edu.cn/')
        self.browserOperator = BrowserOperator(self.driver)
