# import web driver
from selenium import webdriver
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/username/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
# driver.get('https://www.linkedin.com')
def validate_field(field):
    if field:
        pass
    else:
        field = "No result"
    return field

driver.get('https://www.linkedin.com')

username = driver.find_elements(By.ID, "session_key")
username.send_keys("YOUR EMAIL")
sleep(0.5)

password = driver.find_elements(By.ID, "session_password")
password.send_keys("YOUR PASSWORD")
sleep(0.5)

sign_in_button = driver.find_elements(By.XPATH, "//*[@type='submit']")
sign_in_button.click()
sleep(15)

jobdata = []
lnks = []

for x in range(0,20,10):
    driver.get(f'https://www.google.com/search?q=python+developer+in+delli&oq=python+developer+in+delli&aqs=chrome..69i57j35i39l2j0i67i433j0i67i131i433j0i67l2j0i67i433j0i67l2.10529j0j7&sourceid=chrome&ie=UTF-8')