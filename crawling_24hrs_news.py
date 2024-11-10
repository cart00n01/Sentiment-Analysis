import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

listOfHeadlines = []
url = "https://english.onlinekhabar.com/last-24-hours"
options = Options()
options.headless = False
driver = webdriver.Chrome(options = options)
driver.get(url)

headlines = driver.find_elements(By.XPATH, '//div[@class="ok-news-post ltr-post"]/div[@class="ok-post-contents"]/h2/a')
for h in headlines:
    listOfHeadlines.append(h.text)
    # print(h.text)

headDF = pd.DataFrame(listOfHeadlines,columns=['Headlines'])
headDF.to_csv('Last 24 Hours News(Testing Datanew).csv')
print(headDF)




