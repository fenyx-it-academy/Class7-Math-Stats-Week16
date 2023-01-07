#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd


# In[3]:


x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

print(x)
print(x_with_nan)


# In[5]:


math.isnan(np.nan),np.isnan(math.nan)


# In[15]:


y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print("-------y------")
print(y)
print("-------y_with_nan------")
print(y_with_nan)
print("-------z------")
print(z)
print("-------z_with_nan------")
print(z_with_nan)


# In[16]:


mean_ = sum(x) / len(x)
mean_


# In[6]:


# Descriptive Statistics


# In[7]:


#Create a Dictionary of series
d = {'Name':pd.Series(['Ahmet','Mehmet','Ayse','Berk','Mahmut','Aylin','Kazim',
   'Lee','Temel','Gasper','Fatma','Elif']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)


# In[8]:


#Create a DataFrame
df = pd.DataFrame(d)
#summation
print(df.sum())


# In[11]:


#select a column
df['Age'].sum() 


# In[12]:


#apply a desired funtion on specified column(s)
print("----VAR------")
print(df[['Age','Rating']].var())

print("----STD----")
print(df[['Age','Rating']].std())


# In[ ]:


#Sr.No.	Function	Description
#1	count()	Number of non-null observations
#2	sum()	Sum of values
#3	mean()	Mean of Values
#4	median()	Median of Values
#5	mode()	Mode of values
#6	std()	Standard Deviation of the Values
#7	var()	Variance of the Values
#8	min()	Minimum Value
#9	max()	Maximum Value
#10	abs()	Absolute Value
#11	prod()	Product of Values
#12	cumsum()	Cumulative Sum
#13	cumprod()	Cumulative Product


# In[13]:


print(df.describe())


# In[54]:


#Python Pandas - Visualization


# In[26]:


#np.random.seed(123)
df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))
x
df


# In[27]:


df.describe()
#notice on the mean and std


# In[28]:


df.plot()


# In[30]:


#only non zero values
nanzero_df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
nanzero_df.plot.bar()


# In[90]:


nanzero_df.plot.bar(stacked=True)


# In[92]:


#horizontal
nanzero_df.plot.barh(stacked=True)


# In[33]:


df = pd.DataFrame({'a':np.random.randn(1000),'b':np.random.randn(1000),'c':
np.random.randn(1000)}, columns=['a', 'b', 'c'])

#df.plot.hist(bins=20)
df.describe()
df['a'].plot.hist(bins=20)


# In[34]:


df.plot.box()


# In[113]:


df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()


# In[114]:


df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')


# In[116]:


df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)

