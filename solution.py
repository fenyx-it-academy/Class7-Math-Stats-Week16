import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['figure.figsize'] = (8, 5)


food_consumption = pd.read_csv('food_consumption.csv', index_col=0)

print("\n",food_consumption.head(),"\n")


#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

mean = be_consumption['consumption'].mean()
median = be_consumption['consumption'].median()

print(mean)
print(median,"\n")


# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

print(usa_consumption['consumption'].mean())
print(usa_consumption['consumption'].median(),"\n")




# Q-3) Group by country, select consumption column, and compute mean and median
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | 
                              (food_consumption['country'] == 'USA')]

df = pd.DataFrame(be_and_usa)
grouped = df.groupby('country')

# Select the consumption column
consumption = grouped['consumption']

# Calculate the mean and median
mean = consumption.mean()
median = consumption.median()

print(mean,"\n")
print(median,"\n")


rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Create histogram
sns.histplot(rice_consumption["consumption"], bins=69)

# Add labels
plt.xlabel('Rice Consumption')
plt.ylabel('Frequency')
plt.title('Histogram of Rice Consumption')

# Show plot
plt.show()

print(rice_consumption['co2_emission'].agg(['mean','median']),"\n")


# Q-6) Calculate the quintiles of co2_emission
co2_emission = food_consumption['co2_emission']

print(np.quantile(co2_emission, np.linspace(0, 1, 6)),"\n")



# Q-7) Calculate the variance and standard deviation of co2_emission for food_categories

food_category = food_consumption['food_category']
print(food_consumption.groupby('food_category')['co2_emission'].agg(['var','std']),"\n")


# Q-8) Create histogram of co2_emission for food_category 'beef'

beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']

# Create histogram
sns.histplot(beef_consumption["consumption"], bins=32)

# Add labels
plt.xlabel('Beef Consumption')
plt.ylabel('Frequency')
plt.title('Histogram of Beef Consumption')

# Show plot
plt.show()