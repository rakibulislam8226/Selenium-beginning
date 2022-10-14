import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
# driver.get("https://www.tcdb.com") #getting the main url
# driver.get("https://www.tcdb.com/ViewAll.cfm/sp/Baseball") #set url [1]
driver.get("https://www.tcdb.com/ViewAll.cfm/sp/Baseball?MODE=Years") #set url [2]

# search1 = driver.find_elements(By.XPATH, "//*[@id='navbarSupportedContent']/ul[1]/li[1]/ul/a")
# search1 = driver.find_elements(By.XPATH, "//*[@id='content']/div[1]/div[1]/div/ul/li[1]/a")
search1 = driver.find_elements(By.XPATH, "//*[@id='content']/div[1]/div[1]/table[2]/tbody")[0]
search2 = search1.find_elements(By.TAG_NAME, "a")
# print(f"---------search1: {search1}")

out=[]
for item in search2:
    result1={
        "name":item.get_attribute("text"),
        "link":item.get_attribute("href")
    }
    # print(item.get_attribute("innerHTML"))
    out.append(result1)
    
# out=[]
# for item in search1:
#     result1={
#         'link':item.get_attribute("href"),
#     }
#     out.append(result1)

df = pd.DataFrame(out)
df.to_excel('output/set_scrape.xlsx', index=1, header=True)



time.sleep(2)
driver.close()