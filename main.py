from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

promised_down = os.getenv("PROMISED_DOWN")
promised_up = os.getenv("PROMISED_UP")
chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
twitter_email = os.getenv("TWITTER_EMAIL")
twitter_password = os.getenv("TWITTER_PASSWORD")
