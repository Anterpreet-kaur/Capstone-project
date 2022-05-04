#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# ## Objectives
# 

# *   Load the dataset that will used thru the capstone project.
# *   Explore the dataset.
# *   Get familier with the data types.
# 

# ## Load the dataset
# 

# Import the required libraries.
# 

# In[1]:


import pandas as pd


# The dataset is available on the IBM Cloud at the below url.
# 

# In[2]:


dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"


# Load the data available at dataset_url into a dataframe.
# 

# In[3]:


df=pd.read_csv(dataset_url)
df


# ## Explore the data set
# 

# Display the top 5 rows and columns from your dataset.
# 

# In[4]:


df.head()


# ## Find out the number of rows and columns
# 

# Start by exploring the numbers of rows and columns of data in the dataset.
# 

# Print the number of rows in the dataset.
# 

# In[5]:


df.shape[0]


# Print the number of columns in the dataset.
# 

# In[6]:


df.shape[1]


# ## Identify the data types of each column
# 

# Explore the dataset and identify the data types of each column.
# 

# Print the datatype of all columns.
# 

# In[7]:


df.info()


# Print the mean age of the survey participants.
# 

# In[8]:


df['Age'].mean(axis=0)


# The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.
# 

# In[10]:


print('Number of Unique Countries : ', len(df['Country'].unique()))

