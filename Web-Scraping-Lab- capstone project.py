#!/usr/bin/env python
# coding: utf-8

# ## Objectives
# 

# *   Extract information from a given web site
# *   Write the scraped data into a csv file.
# 

# In[1]:


#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


# The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.
# 

# Import the required libraries
# 

# In[2]:


# Your code here
get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests # this module helps us to download a web page
import pandas as pd


# Download the webpage at the url
# 

# In[3]:


#your code goes here
data = requests.get(url).text


# Create a soup object
# 

# In[4]:


#your code goes here
soup = BeautifulSoup(data, 'html5lib')


# Scrape the `Language name` and `annual average salary`.
# 

# In[5]:


#your code goes here
df = pd.DataFrame(columns=['Language Name', 'Average Salary'])

for row in soup.find("tbody").find_all("tr"):
  col = row.find_all("td")
  language = col[1].text
  salary = col[3].text

  df = df.append({'Language Name' : language, 'Average Salary' : salary}, ignore_index=True)

#drop first row
df.drop(index=df.index[0], axis=0, inplace=True)

print(df)


# Save the scrapped data into a file named *popular-languages.csv*
# 

# In[6]:


# your code goes here
df.to_csv('popular-languages.csv')

