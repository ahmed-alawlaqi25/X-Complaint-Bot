import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

URL_SPEED_TEST = "https://www.speedtest.net/"
x_email = os.getenv("EMAIL")
x_password = os.getenv("password")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedXBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options= chrome_options)
        self.down = 0
        self.up =0



    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass








