import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.tcdb.com")
print(driver.title)
# search = driver.find_element(By.CLASS_NAME, "form-group")
# search = driver.find_element(By.ID, "Navigation")
# print(search.get_attribute("innerHTML"))
# print(search.get_attribute("row"))
search1 = driver.find_elements(By.XPATH, "//*[@id='bottomnav']/div[1]/a")
search2 = driver.find_elements(By.XPATH, "//*[@id='bottomnav']/div[2]/a")
search3 = driver.find_elements(By.XPATH, "//*[@id='bottomnav']/div[3]/a")
search4 = driver.find_elements(By.XPATH, "//*[@id='bottomnav']/div[4]/a")

results = {}

out1 = []
for item in search1:
    out1.append(item.text)
results["col1"] = out1
# print(f"---------results, search1: {results}")

out2 = []
for item in search2:
    out2.append(item.text)
results["col2"] = out2

out3 = []
for item in search3:
    out3.append(item.text)
results["col3"] = out3

out4 = []
for item in search4:
    out4.append(item.text)
results["col4"] = out4

# print(f"---------results, search2: {results}")

# df = pd.DataFrame(results, columns=["col1", "col2", "col3", "col4"])
# df = pd.DataFrame.from_dict(results)
df = pd.DataFrame({'col1': pd.Series(out1), 'col2': pd.Series(out2), 'col3': pd.Series(out3), 'col4': pd.Series(out4)})

df.to_excel('output/output.xlsx', index=False, header=True)

time.sleep(2)
driver.close()
