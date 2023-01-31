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

driver.get("https://www.techwithtim.net/")

search = driver.find_element(By.NAME, 's')
search.send_keys("text")
search.send_keys(Keys.RETURN)  # hit the search button.#
# print(search)

# after, search it takes time to load search results and load into another page. in another page I select the main id #
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)

    # individual href for article #
    # articles = main.find_element(By.TAG_NAME, 'article')
    # links = articles.find_elements(By.TAG_NAME, "a")
    # for lnk in links:
    #     print(lnk.get_attribute("href"))

    articles = main.find_elements(By.TAG_NAME, 'article')
    for article in articles:
        # get all the href inside all article #
        # links = article.find_elements(By.TAG_NAME, "a")
        # for lnk in links:
        #     print(lnk.get_attribute("href"))

        header = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(header.text)
finally:
    driver.quit()
