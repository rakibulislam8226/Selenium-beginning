from linkedin_scraper import Company
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/company/spooners-woodworks-inc./")
print(driver.title)
print(driver.page_source.strip())


def checklist():
    card_list = []
    total_len = driver.find_elements(By.CLASS_NAME, "display-flex mt2 mb1")
    print(total_len)
    # print(f'total len {len(total_len)}')
    # for i in range(1, len(total_len) + 1):
    #     a_all = driver.find_elements(By.XPATH, f'//section[1]/div/section[3]/div/ul/li[{i}]/a')
    #     print(f'a all {len(a_all)}')


checklist()
time.sleep(1)
driver.close()
