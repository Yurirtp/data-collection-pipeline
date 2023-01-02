#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time
from time import sleep
from bs4 import BeautifulSoup


if __name__ == "__main__":
    class Scraper:
        
        def __init__(self):
            self.driver = webdriver.Chrome()

        def get_web_page(self):
            self.driver.get("https://uk.indeed.com/")

        def get_new_web_page(self):
            self.driver.get(self.elem)   

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

        def url_links(self):
            #parsed_url = urllib.parse.urlparse(self.driver.current_url)
            self.elems = self.driver.find_elements(by=By.XPATH, value='//*[@class="jcs-JobTitle css-jspxzf eu4oa1w0"]')
            self.url_links_list = [elem.get_attribute('href') for elem in self.elems]
            #self.url_links_list.append(web_url)
            print(self.url_links_list)
                    ## https://www.youtube.com/watch?v=HpLJEGApKEs

        def retrieve_data(self):
            web_s = "https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0A25kp9YPN3MdKWplMFWCpiKNUYRoYgUkIFHWBF1fqov3p11x9regITmqO7RCynW_rYAYB4b9qhT5T1bIyNFuLBxGVNB8fqdZPUBDXJQPpXhrUzKz7_7OBTiDMbERHtAlsNwu-byaZDPUM7ZWhGtnmTz2-2Wsp47VSBgJgpRwiazL1qThLnOVV47b1pYw90-oq5nTNddhsw3cRxjvjI-V5htBKzMNTU3X7LSHGZnE93h_xsU3M8RoBg_45dTCQelofAK1wEj3WOyhNH-2xJdNw7VxxFRqNZyYkEX3RWBcLazX_mHO1n3hc39_kOvLsoSK2vWAcsEyMXiyh4p2a_Q0LZtccJjxkRjwsL6FbHwLge9XhvjypPppEIRNXAlyttqtfHmM6Vp0zmdImLpwZ0U7rslD5q1jHKxRyR9v2khCuNSkM4Wds0NvW-a9drNz02N-y74VM3Sq_KJzDgYrkDgzWKaHDocXEPx1b23T3JUNUqbQ==&xkcb=SoCb-_M3V5nCdAwsYx0LbzkdCdPP&p=0&fvj=1&vjs=3"
            self.driver.get(web_s)
            sleep(3)
            try:
                accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
                accept_cookies_button.click()
            except:
                print("Please try again an Error has occured.")
            image_data = self.driver.find_element(by=By.XPATH, value='//*[@class="jobsearch-CompanyAvatar-image"]')
            image_link = image_data.get_attribute('src')
            print(f'Image link = {image_link}')
            image_2 = self.driver.find_element(by=By.XPATH, value='//*[@class="gnav-header-1rgkyyf eu4oa1w0"]')
            image_link_2 = image_2.get_attribute('src')
            print(f'Image 2 link = {image_link_2}')





def trial():
    web = Scraper()
    web.retrieve_data()

                
        
       





def web_scrape():
    web = Scraper()
    web.get_web_page()
    while True:
        web.accept_cookies()
        web.find_search_bar()
        web.search_input()
        web.url_links()
        break

    
trial()






# %%
