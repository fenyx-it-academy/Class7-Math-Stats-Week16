#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy
import matplotlib.pyplot as plt
import seaborn as sns
 
# number of sample
num = [1, 10, 50, 100] 
# list of sample means
means = [] 
 
# Generating 1, 10, 30, 100 random numbers from -40 to 40
# taking their mean and appending it to list means.
for j in num:
    # Generating seed so that we can get same result
    # every time the loop is run...
    numpy.random.seed(1)
    x = [numpy.mean(
        numpy.random.binomial(
            1, 0.5, j)) for _i in range(1000)]
    means.append(x)
    
k = 0
print(numpy.shape(means))
# plotting all the means in one figure
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        # Histogram for each x stored in means
        
        ax[i, j].hist(means[k], 100, density = True)
        ax[i, j].set_title(label = num[k])
        k = k + 1

plt.show()

#what about binomial distribution?
#[numpy.mean(
        #numpy.random.binomial(
        #    1, 0.5, j)) for _i in range(1000)]

