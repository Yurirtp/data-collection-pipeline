#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from bs4 import BeautifulSoup



class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_web_page(self):
        self.driver.get("https://uk.indeed.com/")

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        height = self.driver.execute_script("return document.documentElement.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, " + str(height) + ");")

    def scroll_page_up(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollTop);")
    
    def find_search_bar(self):
        search_bar = self.driver.find_element(by=By.XPATH, value='//*[@class="icl-TextInput-wrapper"]')
        search_bar.click()
    
    def search_input(self):
        search_bar = self.driver.find_element(by=By.XPATH, value='//*[@class="icl-TextInput-control"]')
        search_bar.send_keys("Junior Data Engineer")
        search_bar.send_keys(Keys.RETURN)
        sleep(5)

    def accept_cookies(self):
        sleep(3)
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
        except:
            print("Please try again an Error has occured.")
        
        
       





def web_scrape():
    web = Scraper()
    web.get_web_page()
    while True:
        web.accept_cookies()
        web.find_search_bar()
        web.search_input()
        sleep(5)
        web.scroll_page_down()
        break

    



web_scrape()



