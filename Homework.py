import pandas as pd
import statistics
import matplotlib.pyplot as plt
import numpy as np


food_consumption = pd.read_csv('/Users/Sansar/Desktop/DS Documents/MathStats-Module-Week16/food_consumption.csv', index_col=0)
print(food_consumption.head())
print()

#####################################################################################################################################

be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

mn1 = statistics.mean(be_consumption['consumption'])
print(mn1)

md1 = statistics.median(be_consumption['consumption'])
print(md1)
print()

usa_consumption = food_consumption[food_consumption['country'] == 'USA']

mn2 = statistics.mean(usa_consumption['consumption'])
print(mn2)

md2 = statistics.median(usa_consumption['consumption'])
print(md2)
print()


#####################################################################################################################################

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
plt.hist(food_consumption['co2_emission'], bins=30)
plt.show()
print()


#####################################################################################################################################

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

rice_mean = statistics.mean(rice_consumption['co2_emission'])
rice_median = statistics.median(rice_consumption['co2_emission'])

df = pd.DataFrame(
    {
        "Mean" : [(rice_mean)], '| '
        "Median" : [(rice_median)]
    }
)

print(df)
print()

#####################################################################################################################################

co2_emission = food_consumption['co2_emission'] 
x = np.quantile(co2_emission, np.linspace(0, 1, 6))
print(x)
print()

#####################################################################################################################################

food_category = food_consumption['food_category']

co2_var = food_consumption.groupby('food_category')['co2_emission'].var()
co2_std = food_consumption.groupby('food_category')['co2_emission'].std()

data = {'co2_var': co2_var,
        'co2_std': co2_std}

df = pd.DataFrame(data)
print(df)
print()

#####################################################################################################################################

co2_beef = food_consumption[food_consumption['food_category'] == 'beef']
plt.hist(food_consumption['co2_emission'], bins=30)
plt.show()
print()