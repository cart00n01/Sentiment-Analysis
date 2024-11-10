import os.path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = "https://english.onlinekhabar.com/category/political"
options = Options()
options.headless = False
driver = webdriver.Chrome(options = options)
driver.get(url)
#getting page title from the online khabar
# pageName = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[1]/div').text#full x path
pageName = driver.find_element(By.XPATH,'//*[@id="primary"]/div[1]/div').text#only x path
# pageName = driver.find_element(By.CLASS_NAME,'ok-inner-page-title').text#only class name
print(pageName)

#getting page number
totalNoofPage = driver.find_elements(By.CLASS_NAME,'page-numbers')
pageNumber = int(totalNoofPage[4].get_attribute('innerHTML'))

#getting the headlines from online khabar
# headlines = driver.find_element(By.XPATH,'//*[@class="ok-post-contents"]/h2/a').text
# headlines = driver.find_elements(By.XPATH,'//*[@class="ok-post-contents"]/h2/a')
# for h in headlines:
#     print(h.text)

headline_list = []
for x in range(1,26):
    newUrl = url+"/page/"+str(x)
    # print(newUrl)
    driver.get(newUrl)
    # headlines = driver.find_elements(By.XPATH,'//*[@class="ok-post-contents"]/h2/a')#problem in this line of code (print small box headline too)
    headlines = driver.find_elements(By.XPATH,'//div[@class="ok-news-post ltr-post"]/div[@class="ok-post-contents"]/h2/a')
    for h in headlines:
        headline_list.append(h.text)
        # print(h.text)

headlinesDf = pd.DataFrame(headline_list,columns=['Headlines'])
headlinesDf['sentiment'] = ''
headlinesDf.to_csv('Headlines of Politics(Training Data(500)).csv')

