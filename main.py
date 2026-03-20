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
        pass


bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()






