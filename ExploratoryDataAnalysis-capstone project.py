#!/usr/bin/env python
# coding: utf-8

# # **Exploratory Data Analysis Lab**
# 

# ## Objectives
# 

# *   Identify the distribution of data in the dataset.
# 
# *   Identify outliers in the dataset.
# 
# *   Remove outliers from the dataset.
# 
# *   Identify correlation between features in the dataset.
# 

# Import the pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")
df


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df.dropna(subset=["ConvertedComp"], axis=0, inplace=True)
df['ConvertedComp'].value_counts().head(20)


# In[6]:


plt.figure(figsize=(12, 7))

sns.distplot(df['ConvertedComp'], hist=False, color="r")

plt.title('Distribution of Developers Salary in USD')
plt.xlabel('Salary converted to annual USD (exchange rate 2019-02-01)')
plt.ylabel('Proportion of Respondents')

plt.show()
plt.close()


# Plot the histogram for the column `ConvertedComp`.
# 

# In[8]:


count, bin_edges = np.histogram(df['ConvertedComp'])

print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins
df['ConvertedComp'].plot(kind='hist', figsize=(20, 5), xticks=bin_edges)

plt.title('Histogram of distribution of Developers\' Annual Salary in USD') # add a title to the histogram
plt.ylabel('Number of Respondents') # add y-label
plt.xlabel('Annual Salary in USD') # add x-label

plt.show()


# What is the median of the column `ConvertedComp`?
# 

# In[7]:


df['ConvertedComp'].median()


# In[9]:


df['Gender'].value_counts()


# How many responders identified themselves only as a **Man**?
# 

# In[10]:


df[df['Gender'] == 'Man'].shape[0]


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[11]:


# your code goes here
df['ConvertedComp'][df['Gender'] == 'Woman'].median()


# In[12]:


df['ConvertedComp'][df['Gender'] == 'Man'].median()
#median ConvertedComp of responders identified themselves only as a Man


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[21]:


df.dropna(subset=["Age"], axis=0, inplace=True)
df['Age'].describe()


# In[22]:


df['Age'].plot(kind='box', figsize=(8, 10))

plt.title('Box plot of Developers\' Age')
plt.ylabel('Age')

plt.show()


# Plot a histogram of the column `Age`.
# 

# In[23]:


count, bin_edges = np.histogram(df['Age'])
print(count)
print(bin_edges)
df['Age'].plot(kind='hist', figsize=(12,7), xticks=bin_edges)
plt.title("Histogram of Developers\' Age WorldWide")
plt.ylabel("Number of Respondents")
plt.xlabel("Age")

plt.show()


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[24]:


df['ConvertedComp'].plot(kind='box', figsize=(8, 10))

plt.title('Box plot of Developers\' Annual Salary in USD')
plt.ylabel('Number of Respondents')

plt.show()


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[25]:


df['ConvertedComp'].describe()
# Q1(25%) = 2.683450e+04
# Q3(75%) = 1.000000e+05
# IQR = Q3 - Q1 = 1.000000e+05 - 2.683450e+04 = 73,165.5


# In[27]:


IQR = df['ConvertedComp'].describe()[6] - df['ConvertedComp'].describe()[4]
IQR


# In[28]:


IQR_V = 1.5 * IQR
IQR_V


# Find out the upper and lower bounds.
# 

# In[29]:


lower = df['ConvertedComp'].describe()[4] - IQR_V
upper = df['ConvertedComp'].describe()[6] + IQR_V

print("Lower bound is:" , lower)
print("Upper bound is:" , upper)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[30]:


# your code goes here
# Using the definition of outlier, any value that is greater than Q3 by 1.5 times or lower than Q1 1.5 times IQR will be flagged as outlier.
# Outlier > 1.000000e+05 + (1.5 * 73,165.5)
# Outlier > 209,748.25

df[(df['ConvertedComp'] > upper) | (df['ConvertedComp'] < lower)].shape[0]


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[31]:


# your code goes here
df_new = df[df['ConvertedComp'] <= upper]
# df_new.drop(['level_0', 'index'], axis=1, inplace=True)
df_new.median()


# In[32]:


df_new.mean()


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[33]:



# your code goes here
import seaborn as sns

corr = df_new.corr()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, cmap=cmap, annot=True, center=0, vmin=-1, square=True, linewidths=.5)
plt.tight_layout()
plt.show()


# In[ ]:




