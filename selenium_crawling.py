import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import requests
import pandas as pd
import time
import logging

# Configure the logging
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
def generate_random_11_digit_number():
    return random.randint(10**10, 10**11 - 1)

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        logging.info("Internet connection is available.")
        return True
    except requests.ConnectionError:
        logging.error("Internet connection is not available.")
        return False
    except requests.Timeout:
        logging.error("Request to Google timed out. Check your internet connection.")
        return False
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return False

delay = 3

while True:
    if not check_internet_connection():
        time.sleep(delay)
        continue
    clubs = {}
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    
    try:
        random_number = generate_random_11_digit_number()
        url = f"https://find.englandfootball.com/club/{random_number}"
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(delay)
        time.sleep(delay)
        
        all_cookies = driver.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        
        driver.get(url)
        logging.info(driver)
        response = requests.get(url, cookies=cookies_dict).text
        soup = BeautifulSoup(response, "html.parser")
        
        club_name = soup.title.text
        
        if club_name == "Discover Football":
            continue
        else:
            clubs["name"] = club_name
            df = pd.DataFrame.from_dict(clubs)
            df.to_csv("club_results.csv")
            logging.info(f"Club '{club_name}' data written to CSV.")
    except Exception as e:
        logging.error(f"An error occurred while processing URL '{url}': {e}")