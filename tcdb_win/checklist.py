import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.tcdb.com/Checklist.cfm/sid/231617/1866-Newberry-&-Solanders")


def checklist():
    card_list = []
    total_len = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr")

    for i in range(1, len(total_len) + 1):
        a_all = driver.find_elements(By.XPATH, f'//*[@id="content"]/div[2]/div[1]/table[2]/tbody/tr[{i}]/td/a')

        # print(f"----------a_all: {a_all}")
        # count = 0
        # for tag in a_all:
        #     count += 1
        #     print(f"{i}. ----------{count}. >> tag: {tag.get_attribute('href')}")

        card_dict = dict()
        team = a_all[-1].get_attribute("href")
        if team is not None:
            card_dict['team'] = team
        player = a_all[-2].get_attribute("href")
        string_player = 'https://www.tcdb.com/Person.cfm/pid'
        if string_player in player:
            card_dict['player'] = player

        card = a_all[2].get_attribute("href")

        # print(f"row %d ---------{tab2}" % i)
        card_list.append(card_dict)

    df = pd.DataFrame(card_list)
    df.to_excel('output/card_list.xlsx', index=True, header=True)


checklist()
time.sleep(2)
driver.close()
