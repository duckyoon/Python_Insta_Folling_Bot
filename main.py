from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PWD = os.getenv('PWD')
SIMILIAR = "runningfischi"

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(path)
        time.sleep(5)
        
    def login(self, ):
        input_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        input_name.click()
        input_name.send_keys(USER_NAME)
        time.sleep(1)
        
        input_pwd = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        input_pwd.click()
        input_pwd.send_keys(PWD)
        time.sleep(1)
    
        click_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        click_login.click()
        time.sleep(3)
        
    def find_followers(self, ):
        search = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div')
        search.click()
        time.sleep(2)
        
        search_running = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search_running.click()
        search_running.send_keys('running')
        time.sleep(2)
        
        select_first = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
        select_first.click()
        time.sleep(2)

        open_follow = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        open_follow.click()
        time.sleep(2)
        
        #스크롤
        for _ in range(10):
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        
    def follow(self, ):
        follows = self.driver.find_elements(By.CSS_SELECTOR, "div div button")
        for follow in follows:
            try:
                follow.click()
                time.sleep(3)
            except :
                pass
    
# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
path = "https://www.instagram.com/"

# 클래스 호출
insta = InstaFollower(path)
insta.login()
insta.find_followers()
insta.follow()
