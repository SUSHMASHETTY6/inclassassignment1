#!/usr/bin/env python
# coding: utf-8

# In[3]:


#question 1

from numpy import random;
import numpy as np;
a=random.randint(20, size=(15))
#Reshape the array to 3 by 5
b = a.reshape(3,5)
#Print array shape.
print(b)
print(b.shape)
#Replace the max in each row by 0
new_a = np.where(b == [
   [i]
   for i in np.amax(b, axis = 1)
], 0 ,b)
print(new_a)


# In[15]:


#question 2

import pandas as pd
#Read the provided CSV file ‘data.csv’.
df=pd.read_csv("./data.csv")
#Replace the null values with the mean
mean_value=df['Calories'].mean()
df['Calories'].fillna(value=mean_value,inplace=True)
df.head(25)






a


# In[6]:


#Select at least two columns and aggregate the data using: min, max, count, mean.
df.Duration.describe()


# In[8]:


df.Pulse.describe()


# In[9]:


# Filter the dataframe to select the rows with calories values between 500 and 1000. 
df[(df['Calories']>500) & (df['Calories']<1000)]


# In[20]:


# Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
df[(df['Calories']>500 & (df['Pulse']<100))]


# In[ ]:


# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified=df.drop("Maxpulse",axis=1)


# In[25]:


df_modified


# In[ ]:


# Delete the “Maxpulse” column from the main df dataframe
df=df.drop("Maxpulse",axis=1)


# In[19]:


df


# In[26]:


# Convert the datatype of Calories column to int datatype.
df['Calories']=df['Calories'].astype(int)


# In[3]:


df.dtypes


# In[ ]:





# In[2]:


# Using pandas create a scatter plot for the two columns (Duration and Calories)
df.plot.scatter( x = 'Duration', y = 'Calories')


# In[ ]:





# In[27]:


#question 3
# Write a Python programming to create a below chart of the popularity of programming Languages
prgmng_df=pd.DataFrame({"popularity":[22.2, 17.6, 8.8, 8, 7.7, 6.7]},index=['Java','Python','PHP','JavaScript', 'C#', 'C++'])
prgmng_df


# In[2]:



# pi chart
import matplotlib.pyplot as plt
#language plotting
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
#popularity_plotting
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
#colors_plotting
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
#explode 1st slice
explode = (0.1, 0, 0, 0,0,0)
#plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[ ]:




