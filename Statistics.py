import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
from matplotlib import pyplot


food_consumption = pd.read_csv('food_consumption.csv', index_col=0)
food_consumption.head()
#print (food_consumption)

#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

usa_consumption.head()
print(be_consumption)

#Calculate mean and median consumption in Belgium

be_mean = sum(be_consumption.consumption) / len (be_consumption.consumption)
print(f'Belgium consumption mean = {be_mean}')

usa_mean = sum(usa_consumption.consumption) / len (usa_consumption.consumption)
print(f'USA consumption mean = {usa_mean}')

be_median = np.median(be_consumption.consumption)
print(f'Belgium consumption median = {be_median}')

usa_median = np.median(usa_consumption.consumption)
print(f'USA consumption median = {usa_median}')

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

#Calculate mean and median of co2_emission with .agg()
print(rice_consumption)
rice_median = np.median(rice_consumption.co2_emission)
print(f'Rice CO2 median emission = {rice_median}')

rice_mean = sum(rice_consumption.co2_emission) / len (rice_consumption.co2_emission)
print(f'Rice CO2 mean emission = {rice_mean}')

print(food_consumption.groupby(["food_category"])["co2_emission"].median())
print(food_consumption.groupby(["food_category"])["co2_emission"].mean())

#Plot the histogram of co2_emission for rice
pyplot.plot (rice_consumption.co2_emission)
pyplot.show ()

#Calculate the quintiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 6)))

#Calculate the variance and standard deviation of co2_emission for food_categories
print(food_consumption.groupby(["food_category"])["co2_emission"].var())
print(food_consumption.groupby(["food_category"])["co2_emission"].std())

#Create histogram of co2_emission for food_category 'beef'
beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']
#pyplot.plot (food_consumption.food_category.beef)
pyplot.plot(beef_consumption.co2_emission)
pyplot.show ()

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
print(emissions_by_country)

q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country > upper) | (emissions_by_country < lower)]
print(outliers)