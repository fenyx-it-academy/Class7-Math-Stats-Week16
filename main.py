import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)

food_consumption = pd.read_csv('/Users/rumeysayakar/Desktop/derslik/statistic/Class7-MathStats-Module-Week16/food_consumption.csv', index_col=0)
food_consumption.head()

#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']


# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']


# Q-1) Calculate mean and median consumption in Belgium
mean_of_belgium = np.mean(be_consumption['consumption'])
median_of_belgium = np.median(be_consumption['consumption'])
print(mean_of_belgium)
print(median_of_belgium)


# Q-2) Calculate mean and median consumption of USA
mean_of_usa = np.mean(usa_consumption['consumption'])
median_of_usa = np.median(usa_consumption['consumption'])
print(mean_of_usa)
print(median_of_usa)


# # Work with both countries together
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | 
                              (food_consumption['country'] == 'USA')]


# # Q-3) Group by country, select consumption column, and compute mean and median
group_be_and_usa = be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median])
print(group_be_and_usa)


rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
# Q-4)Plot the histogram of co2_emission for rice
rice_consumption['co2_emission'].hist()
# Q-5) Calculate mean and median of co2_emission with .agg()
co2_mean_and_median = rice_consumption['co2_emission'].agg([np.mean, np.median])
print(co2_mean_and_median)


# Q-6) Calculate the quintiles of co2_emission
co2_quintiles = np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6))
print(co2_quintiles)

# Q-7) Calculate the variance and standard deviation of co2_emission for food_categories
var_and_std = food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std])
print(var_and_std)

# Q-8) Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()

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