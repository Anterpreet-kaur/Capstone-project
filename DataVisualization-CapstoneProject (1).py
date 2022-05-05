#!/usr/bin/env python
# coding: utf-8

# # **Data Visualization Lab**
# 

# ## Objectives
# 

# *   Visualize the distribution of data.
# 
# *   Visualize the relationship between two features.
# 
# *   Visualize composition of data.
# 
# *   Visualize comparison of data.
# 

# <hr>
# 

# ## Demo: How to work with database
# 

# Download database file.
# 

# In[ ]:


get_ipython().system('wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite')


# Connect to the database.
# 

# In[30]:


import sqlite3
conn = sqlite3.connect("m4_survey_final_data.sqlite") # open a database connection


# In[31]:


conn


# Import pandas module.
# 

# In[32]:




import pandas as pd


# ## Demo: How to run an sql query
# 

# In[33]:


# print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""

# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
df.head()


# ## Demo: How to list all tables
# 

# In[34]:


# print all the tables names in the database
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
pd.read_sql_query(QUERY,conn)


# In[35]:


QUERY = """
SELECT DevType, count(DevType) as c1
FROM DevType
group by DevType
order by c1 DESC
"""
pd.read_sql_query(QUERY,conn)


# ## Demo: How to run a group by query
# 

# In[36]:


QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
pd.read_sql_query(QUERY,conn)


# ## Demo: How to describe a table
# 

# In[37]:


table_name = 'master'  # the table you wish to describe

QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0])


# In[38]:


QUERY = """
SELECT Employment
FROM master
"""
pd.read_sql_query(QUERY,conn)


# # Hands-on Lab
# 

# ## Visualizing distribution of data
# 

# ### Histograms
# 

# Plot a histogram of `ConvertedComp.`
# 

# In[39]:


import seaborn as sns

QUERY = """
SELECT *
FROM master
"""
df = pd.read_sql_query(QUERY,conn)
ax = sns.histplot(df['ConvertedComp'])


# ### Box Plots
# 

# Plot a box plot of `Age.`
# 

# In[40]:



ax = sns.boxplot(x=df_Age['Age'])


# ## Visualizing relationships in data
# 

# ### Scatter Plots
# 

# Create a scatter plot of `Age` and `WorkWeekHrs.`
# 

# In[41]:


# your code goes here

ax = sns.scatterplot(data=df, x='Age', y='WorkWeekHrs')


# ### Bubble Plots
# 

# Create a bubble plot of `WorkWeekHrs` and `CodeRevHrs`, use `Age` column as bubble size.
# 

# In[43]:



ax = sns.scatterplot(data=df, x='WorkWeekHrs', y='CodeRevHrs', size='Age', hue='Age', sizes=(20,200))


# In[45]:


QUERY = """
SELECT Age, ConvertedComp
FROM master
WHERE Age >= 30 AND Age <= 35
"""
df = pd.read_sql_query(QUERY, conn)
ax = sns.scatterplot(data=df, x='Age', y='ConvertedComp', size='Age', hue='Age', sizes=(20,200))


# ## Visualizing composition of data
# 

# ### Pie Charts
# 

# Create a pie chart of the top 5 databases that respondents wish to learn next year. Label the pie chart with database names. Display percentages of each database on the pie chart.
# 

# In[47]:


# your code goes here

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
QUERY = """
SELECT DatabaseDesireNextYear, count(*) as c1
FROM DataBaseDesireNextYear
group by DatabaseDesireNextYear
order by c1 DESC
"""
df = pd.read_sql_query(QUERY, conn)


# Create the chart
labels = df['DatabaseDesireNextYear'].head(5)
sizes = df['c1'].head(5)
explode = (0,0,0,0,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # equal so pie will be drawn as circle

plt.show()


# ### Stacked Charts
# 

# Create a stacked chart of median `WorkWeekHrs` and `CodeRevHrs` for the age group 30 to 35.
# 

# In[25]:


# your code goes here

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

QUERY = """
SELECT WorkWeekHrs, CodeRevHrs, Age
FROM master
WHERE age <= 35 AND age >= 30
order by age
"""

df = pd.read_sql_query(QUERY, conn)

l1 = [30,31,32,33,34,35]
l2 = []
l3 = []

for i in l1:
    l2.append(df[df['Age']==i]['WorkWeekHrs'].median())
    l3.append(df[df['Age']==i]['CodeRevHrs'].median())

# Chart
labels = l1
y1 = l2
y2 = l3

plt.bar(labels, y1, color='r')
plt.bar(labels, y2, bottom=y1, color='b')
plt.legend(['WorkWeekHrs', 'CodeRevHrs'])
plt.xlabel('Age')
plt.ylabel('Hours')
plt.title('WorkWeek hours & CodeRevHrs')
plt.show()


# ## Visualizing comparison of data
# 

# ### Line Chart
# 

# Plot the median `ConvertedComp` for all ages from 45 to 60.
# 

# In[26]:


# your code goes here
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

QUERY = """
SELECT ConvertedComp, Age
FROM master
WHERE age <= 60 AND age >= 45
order by age
"""

df = pd.read_sql_query(QUERY, conn)

l1 = range(45, 60)
l2 = []

for i in l1:
    l2.append(df[df['Age']==i]['ConvertedComp'].median())

# Line chart
plt.figure()
plt.plot(l1, l2)

plt.xlabel('Age')
plt.ylabel('US$')
plt.title('ConvertedComp & Age')
plt.grid(True, linestyle='--')

plt.show()


# ### Bar Chart
# 

# Create a horizontal bar chart using column `MainBranch.`
# 

# In[27]:


# your code goes here
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

QUERY = """
SELECT MainBranch
FROM master
group by MainBranch
"""

df = pd.read_sql_query(QUERY, conn)
df.head()


# Close the database connection.
# 

# In[48]:


conn.close()

