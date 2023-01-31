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


def click_navigation():
    driver.get("https://www.techwithtim.net/")

    link = driver.find_element(By.LINK_TEXT, 'Python Programming')
    link.click()

    try:
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Intermediate Python Tutorials"))
        )
        element1.click()

        element2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sow-button-19310003"))
        )
        element2.click()

        # get one page back and again go forward on that page #
        driver.back()
        driver.forward()

    except:
        driver.quit()


click_navigation()
time.sleep(5)
