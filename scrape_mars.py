
# coding: utf-8

# # Mission to Mars - Step1
# 
# from bs4 import BeautifulSoup
# from splinter import Browser
# import pandas as pd
# import requests
# import pymongo
# import time
# from selenium import webdriver
# 
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# 
# db = client.missionmars_db
# collection = db.items

# In[3]:


#Set up splinter

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless=False)


# In[4]:


# URL of page to be scraped - NASA Mars News

url = "https://mars.nasa.gov/news/"
browser.visit(url)
time.sleep(1)

# Create Beautiful Soup object; parse with html.parser

html = browser.html
soup = BeautifulSoup(html, "html.parser")

news_title = soup.find('div', class_='content_title').text
news_p = soup.find('div', class_='article_teaser_body').text
print(news_title)
print(news_p)


# In[5]:


# URL of page to be scraped - JPL

browser = Browser('chrome', headless = False)

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
time.sleep(2)

browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)

browser.click_link_by_partial_text('more info')

jpl_html = browser.html
soup = BeautifulSoup(jpl_html, "html.parser")

img_path = soup.find('figure', class_='lede').find('img')['src']
featured_image_url = "https://www.jpl.nasa.gov/" + img_path

browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)

browser.click_link_by_partial_text('more info')
time.sleep(2)

jpl_html = browser.html
spaceimage = BeautifulSoup(jpl_html, 'html.parser')

featured_image = spaceimage.find('figure', class_='lede').find('img')['src']
print(featured_image )


# In[6]:


print(featured_image_url)


# In[8]:


# URL of page to be scraped - MARS Weather

browser = Browser('chrome', headless = False)

url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)
time.sleep(2)

mars_weather_html = browser.html
soup = BeautifulSoup(mars_weather_html, 'html.parser')

marsweather = soup.find('div', class_='js-tweet-text-container')
mars_weather = marsweather.find('p', class_='TweetTextSize').text
print(mars_weather)


# In[11]:


# MARS Facts

url = 'https://space-facts.com/mars/'
browser.visit(url)
time.sleep(2)

mars_facts_html = browser.html
soup = BeautifulSoup(mars_facts_html, 'html.parser')

mars_tables = pd.read_html(url)

marsdf = mars_tables[0]
marsdf.columns = ['Description', 'Value']

marsdf


# In[16]:


# convert to html table string using Pandas

mars_table_html = marsdf.to_html(header = False, index = False)
print(mars_table_html)



# In[21]:


# Mars Hemispheres

browser = Browser("chrome", headless=False)

base_url = "https://astrogeology.usgs.gov"

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

mars_html = browser.html
soup = BeautifulSoup(mars_html, 'html.parser')

hemi_image_url = []

hemispheres = soup.find_all('div', class_="description")

for hemisphere in hemispheres:
   
    image_title = hemisphere.h3.text
    hem_url = base_url + hemisphere.a['href']
    browser.visit(hem_url) 
    time.sleep(2)
    
    image_html = browser.html
    soup = BeautifulSoup(image_html, 'html.parser')
    image_url = soup.find('div', class_='downloads').find('li').a['href']

    #Save image and title in a dictionary 
    hemisphere_dict = {}
    hemisphere_dict = {'title' : image_title, 'img_url' : image_url}

    #append dictionary
    hemi_image_url.append(hemisphere_dict)

print(hemi_image_url)


# # Mission to Mars - Step 2
