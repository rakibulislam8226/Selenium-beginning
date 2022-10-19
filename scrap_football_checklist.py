import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.tcdb.com/Checklist.cfm/sid/124068/1894-Mayo-Cut-Plug-(N302)")


def checklist():
    card_list = []
    total_len = driver.find_elements(By.XPATH, '//*[@id="content"]/div[2]/div[1]/table[2]/tbody/tr')
    for i in range(1, len(total_len) + 1):
        a_all = driver.find_elements(By.XPATH, f'//*[@id="content"]/div[2]/div[1]/table[2]/tbody/tr[{i}]/td/a')
        card_dict = dict()

        player_name = a_all[4].text
        if player_name is not None:
            card_dict['player_name'] = player_name

        player_url = a_all[-2].get_attribute("href")
        if player_url is not None:
            card_dict['player url'] = player_url

        card_url = a_all[2].get_attribute("href")
        if card_url is not None:
            card_dict['card url'] = card_url

        team = a_all[-1].get_attribute("href")
        if team is not None:
            card_dict['team'] = team

        card_list.append(card_dict)

    df = pd.DataFrame(card_list)
    df.to_excel('output/football_checklist.xlsx', index=True, header=True)


checklist()
time.sleep(2)
driver.close()
