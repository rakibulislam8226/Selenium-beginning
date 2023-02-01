import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("https://www.linkedin.com/company/spooners-woodworks-inc./")
driver.get("https://www.linkedin.com/")

username = driver.find_element(By.NAME, "session_key")
username.send_keys("mediusware.seo@gmail.com")

password = driver.find_element(By.NAME, "session_password")
password.send_keys("Cq9c$@2F)=ZG-Eg")

sign_in = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
sign_in.click()

print("success")

time.sleep(5)
driver.quit()
