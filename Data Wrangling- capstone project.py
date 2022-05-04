#!/usr/bin/env python
# coding: utf-8

# ## Objectives
# 

# *   Identify duplicate values in the dataset.
# 
# *   Remove duplicate values from the dataset.
# 
# *   Identify missing values in the dataset.
# 
# *   Impute the missing values in the dataset.
# 
# *   Normalize data in the dataset.
# 

# Import pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")
df


# ## Finding duplicates
# 

# In this section you will identify duplicate values in the dataset.
# 

# Find how many duplicate rows exist in the dataframe.
# 

# In[19]:


df.duplicated().sum()


# ## Removing duplicates
# 

# Remove the duplicate rows from the dataframe.
# 

# In[20]:


df.drop_duplicates(inplace=True)


# Verify if duplicates were actually dropped.
# 

# In[21]:


df.duplicated().sum()


# In[22]:


df


# ## Finding Missing values
# 

# Find the missing values for all columns.
# 

# In[23]:


missing_data = df.isnull()
missing_data.head()
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 


# Find out how many rows are missing in the column 'WorkLoc'
# 

# In[24]:


print(missing_data['WorkLoc'].value_counts())


# ## Imputing missing values
# 

# Find the  value counts for the column WorkLoc.
# 

# In[25]:


df['WorkLoc'].value_counts()


# Identify the value that is most frequent (majority) in the WorkLoc column.
# 

# In[26]:


#make a note of the majority value here, for future reference
#
df['WorkLoc'].value_counts().idxmax()


# In[27]:


df['WorkLoc'].replace(np.nan, 'Office', inplace=True)


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# 

# After imputation there should ideally not be any empty rows in the WorkLoc column.
# 

# Verify if imputing was successful.
# 

# In[28]:


print(df['WorkLoc'].value_counts(dropna=False))


# In[29]:


df['Employment'].value_counts().idxmax()


# In[30]:


df['UndergradMajor'].value_counts()


# ## Normalizing data
# 

# There are two columns in the dataset that talk about compensation.
# 
# One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
# 
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq".
# 
# This makes it difficult to compare the total compensation of the developers.
# 
# In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
# 
# Once this column is ready, it makes comparison of salaries easy.
# 

# <hr>
# 

# List out the various categories in the column 'CompFreq'
# 

# In[32]:


df['CompFreq'].value_counts()


# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
# 

# In[33]:


# your code goes here
def conditions(s):
  if (s['CompFreq'] == 'Yearly'):
    return s['CompTotal']
  elif (s['CompFreq'] == 'Monthly'):
    return (s['CompTotal'] * 12)  
  else:
    return (s['CompTotal'] * 52)

df['NormalizedAnnualCompensation'] = df.apply(conditions, axis=1)
df.head()


# In[34]:


df[['CompFreq', 'CompTotal', 'NormalizedAnnualCompensation']].head()


# In[35]:


df['NormalizedAnnualCompensation'].describe()

