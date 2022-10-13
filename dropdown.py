import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.tcdb.com")

# dropdown1 = driver.find_element(By.NAME, "SearchCategory")
# drp=Select(dropdown1).options
# print(drp)
# for options in drp:
#     print(options)

dropdown1 = driver.find_elements(By.XPATH, "//*[@id='navbarSupportedContent']/ul[1]/li[1]/ul/a")
out=[]
for item in dropdown1:
    result1={
        'name':item.get_attribute("text"),
        'link':item.get_attribute("href"),
    }
    out.append(result1)

df = pd.DataFrame(out)
df.to_excel('output/dropdown.xlsx', index=False, header=True)


time.sleep(2)
driver.close()