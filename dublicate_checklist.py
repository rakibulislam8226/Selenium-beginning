import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.tcdb.com/ViewSet.cfm/sid/2006/1948-Bowman")


def checklist():
    card_list = []
    # total_len = driver.find_elements(By.XPATH, '//*[@id="content"]/div[1]/div[2]/table/tbody/tr')
    # for i in range(1, len(total_len) + 1):
    #     link = driver.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[2]/table/tbody/tr[{i}]/td')
    #     all_a = link.find_elements(By.TAG_NAME, '/a')
    #     # print(all_a)
    #     # print(f"----------a_all: {all_a}")
    #     count = 0
    #     for tag in all_a:
    #         count += 1
    #         print(f"{i}. ----------{count}. >> tag: {tag.get_attribute('href')}")

    # df = pd.DataFrame(card_list)
    # df.to_excel('output/dub_check.xlsx', index=True, header=True)

    check = driver.find_element(By.TAG_NAME, '//h1')

    if check is not None:
        print(check)
    print("not found")


checklist()
time.sleep(2)
driver.close()
