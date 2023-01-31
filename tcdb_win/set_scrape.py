import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
# driver.get("https://www.tcdb.com") #getting the main url
# driver.get("https://www.tcdb.com/ViewAll.cfm/sp/Baseball") #set url [1]
# driver.get("https://www.tcdb.com/ViewAll.cfm/sp/Baseball?MODE=Years") #set url [2]
driver.get("https://www.tcdb.com/Checklist.cfm/sid/231617/1866-Newberry-&-Solanders") #set url fo card[3]

# search1 = driver.find_elements(By.XPATH, "//*[@id='navbarSupportedContent']/ul[1]/li[1]/ul/a")
# search1 = driver.find_elements(By.XPATH, "//*[@id='content']/div[1]/div[1]/div/ul/li[1]/a")
# search1 = driver.find_elements(By.XPATH, "//*[@id='content']/div[1]/div[1]/table[2]/tbody")[0]
# search2 = search1.find_elements(By.TAG_NAME, "a")
search3 = driver.find_elements(By.XPATH, "//*[@id='content']/div[2]/div[1]/table[2]/tbody/tr")
# search4 = search3.find_elements(By.TAG_NAME, "a")
search6 = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr/td/a[2]")
search7 = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr[1]/td/a")
# players = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr/td[27]/a")
play = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr/td[17]/a")
image = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr/td/a[2]")
teams = driver.find_elements(By.XPATH, "//div[2]/div[1]/table[2]/tbody/tr/td[39]/a")
players = driver.find_elements(By.XPATH, "//*[@id='content']/div[2]/div[1]/table[2]/tbody/tr[1]/td[17]/a")
# search7 = search6.find_elements(By.TAG_NAME, "a")


results={}
unique_list = []
for play in players:
    a=play.get_attribute('href')
    b= play.get_attribute('text')
    if b=="NNO":
        continue
    elif b==b:
        print(f"paisi {b}")

    elif a not in unique_list:
        unique_list.append(a)
        # print(f"title ------- {a}")


for p in play:
    a=p
    print(f"player======== {a}")
    if a:
        print(f"player======== {a}")
        

        
####### for cards image  ########   
unique_image = []
for img in image:
    im=img.get_attribute('href')
    # print(f"image======== {im}")
    unique_image.append(im)
results["ImageURL"] = unique_image

####### for cards players  ########   
player = []
for p in players:
    play=p.get_attribute('href')
    # print(f"player======== {play}")
    player.append(play)
results["PlayerURL"] = player


####### for cards team  ########   
# unique_team = []
for team in teams:
    tea=team.get_attribute('href')
    # print(f"team======== {tea}")
#     unique_team.append(tea)
# results["TeamURL"] = unique_team



# Type_new = pd.Series([],dtype=pd.StringDtype()) 
# df = pd.DataFrame({'PlayerURL': pd.Series(player_list)})

# df.to_excel('output/set_scrape.xlsx', index=1, header=True)
    

# for search in search6:
#     print(search.get_attribute('href'))
# for searcha in search7:
#     if searcha.text=="NNO":
#         continue
#     elif searcha.text:
#         print(f"---------  {searcha.text}")

# for player in players:
#     print(player.get_attribute('href'))
    


# out=[]
# results={}
# for item in search3:
#     out.append(item.text)
# results["Name"] = out

# out2=[]
# for item in search6:
#     out2.append(item.get_attribute('herf'))
# results["Team"] = out2
# print(f"---------results, search1: {results}")

# for item in search4:
#     result1={
#         "link":item.get_attribute("href")
#     }
#     out.append(result1)

# out=[]
# for item in search2:
#     result1={
#         "name":item.get_attribute("text"),
#         "link":item.get_attribute("href")
#     }
#     out.append(result1)
    
# out=[]
# for item in search1:
#     result1={
#         'link':item.get_attribute("href"),
#     }
#     out.append(result1)

# df = pd.DataFrame(out)
# df.to_excel('output/set_scrape.xlsx', index=1, header=True)



time.sleep(1)
driver.close()