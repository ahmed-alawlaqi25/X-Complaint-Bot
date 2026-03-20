import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

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
        self.driver.get(URL_SPEED_TEST)
        go = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go.click()
        
         while True:
        download_speed = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "download-speed")))
        upload_speed = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed")))

        if download_speed.text and upload_speed.text != "—":
            print(download_speed.text)
            print(upload_speed.text)
            break
        sleep(1)


    def tweet_at_provider(self):
        self.driver.get(URL_X)
        sleep(random.uniform(1.5, 3.0))
        email_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "r-30o5oe")))
        email_input.send_keys(X_EMAIL)
        sleep(random.uniform(1.5, 3.0))
        next_step = self.driver.find_element(By.CLASS_NAME, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_step.click()
        sleep(random.uniform(1.5, 3.0))

        input_field = self.driver.find_element(By.CLASS_NAME, value='public-DraftStyleDefault-block')
        input_field.send_keys(
            f"This is a Test of the twitter interface, my current upload speed is {self.up} and down is {self.down}\n")
        post_button = self.driver.find_element(By.CSS_SELECTOR, value='button[data-testid="tweetButtonInline"]')
        post_button.click()


bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()






