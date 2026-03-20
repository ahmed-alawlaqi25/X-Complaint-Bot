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


          # wait up to 10 seconds

        speed = self.wait.until(
            lambda d: d.find_element(By.CLASS_NAME, "download-speed").text != "—"
        )
        # speeds = self.driver.find_element(By.CLASS_NAME, "download-speed")
        print(speed)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()






