#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python 

# # (A part of Big Data Analysis)

# -----

# # The Weather Dataset
# ***
# Here, 
# The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
# 
# 
# This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.

# In[29]:


import pandas as pd


# In[30]:


data = pd.read_csv(r"1. Weather Data.csv")


# In[31]:


data


# # How to Analyze DataFrames ?

# # .head()
# It shows the first N rows in the data (by default, N=5).

# In[32]:


data.head()


# # .shape
# 
# It shows the total no. of rows and no. of columns of the dataframe

# In[33]:


data.shape


# # .index
# This attribute provides the index of the dataframe

# In[35]:


data.index


# # .columns
# It shows the name of each column

# In[36]:


data.columns


# # .dtypes
# It shows the data-type of each column 

# In[37]:


data.dtypes


# # .unique()
# In a column, it shows all the unique values. 
# It can be applied on a single column only, not on the whole dataframe.

# In[38]:


data['Weather'].unique()


# # .nunique()
# It shows the total no. of unique values in each column. 
# It can be applied on a single column as well as on whole dataframe.

# In[39]:


data.nunique()


# # .count 
# It shows the total no. of non-null values in each column. 
# It can be applied on a single column as well as on whole dataframe.

# In[40]:


data.count()


# # .value_counts
# In a column, it shows all the unique values with their count. It can be applied on single column only.

# In[41]:


data['Weather'].value_counts()


# # .info()
# Provides basic information about the dataframe.

# In[42]:


data.info()


# -----

# # Q) 1.  Find all the unique 'Wind Speed' values in the data.

# In[49]:


data.head(2)


# In[50]:


data.nunique()


# In[51]:


data['Wind Speed_km/h'].nunique()


# In[52]:


data['Wind Speed_km/h'].unique() # Answer


# # Q) 2. Find the number of times when the 'Weather is exactly Clear'.

# In[53]:


data.head(2)


# In[54]:


# value_counts()
data.Weather.value_counts()


# In[57]:


# Filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[59]:


# groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# # Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[60]:


data.head(2)


# In[63]:


data[data['Wind Speed_km/h'] == 4] # Answer


# # Q. 4) Find out all the Null Values in the data.

# In[65]:


data.isnull().sum()


# In[66]:


data.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[67]:


data.head(2)


# In[70]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[71]:


data.head()


# # Q.6) What is the mean 'Visibility' ?

# In[72]:


data.head(2)


# In[73]:


data.Visibility_km.mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[74]:


data.Press_kPa.std()


# # Q. 8) Whats is the Variance of 'Relative Humidity' in this data ?

# In[75]:


data['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[79]:


# value_counts()
#data.head(2)
data['Weather Condition'].value_counts()


# In[80]:


#Filtering
data[data['Weather Condition'] == 'Snow'] #.loc


# In[87]:


# str.contains
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[88]:


data.head(2)


# In[89]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Conditon' ?

# In[90]:


data.head(2)


# In[91]:


data.groupby('Weather Condition').mean()


# In[ ]:





# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?

# In[92]:


data.head(2)


# In[93]:


data.groupby('Weather Condition').min()


# In[94]:


data.groupby('Weather Condition').max()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[95]:


data[data['Weather Condition'] == 'Fog']


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[98]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].tail(50)


# # Q. 15) Find all instances when :
# ### A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# ### or
# ### B. 'Visibility is above 40'

# In[99]:


data.head(2)


# In[101]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)]

