from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
import time


load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PWD = os.getenv('PWD')
SIMILIAR = "runningfischi"

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(path)
        time.sleep(2)
        
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
        pass
    
    def follow(self, ):
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
