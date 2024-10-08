import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv()

promised_down = os.getenv("PROMISED_DOWN")
promised_up = os.getenv("PROMISED_UP")
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
twitter_email = os.getenv("TWITTER_EMAIL")
twitter_password = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        button = self.driver.find_element(By.CLASS_NAME, "start-text")
        button.click()

        time.sleep(60)

        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                             '1]/div/div['
                                                             '2]/span').text)
        self.up = float(
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                               '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get('https://x.com/i/flow/login')

        time.sleep(5)
        email = self.driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]')
        email.send_keys(twitter_email, Keys.ENTER)
        time.sleep(10)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(twitter_password, Keys.ENTER)
        time.sleep(5)



bot = InternetSpeedTwitterBot()
#bot.get_internet_speed()
bot.tweet_at_provider()
