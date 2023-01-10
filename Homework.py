import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


food_consumption = pd.read_csv('food_consumption.csv', index_col=0)
# print(food_consumption.head(), ' \n')

#####################################################################################################################################

# be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# mn1 = statistics.mean(be_consumption['consumption'])
# print('Mean For Belgium: ', mn1, )

# md1 = statistics.median(be_consumption['consumption'])
# print('Median For Belgium: ', md1, ' \n')


# usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# mn2 = statistics.mean(usa_consumption['consumption'])
# print('Mean For USA: ', mn2)

# md2 = statistics.median(usa_consumption['consumption'])
# print('Median For USA: ', md2, ' \n')



#####################################################################################################################################
# rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# # Group the data by country and calculate the sum of CO2 emissions for each country
# armut=rice_consumption[["country","co2_emission"]]
# co2_emission_by_country = rice_consumption.groupby('country')['co2_emission'].sum().reset_index()

# # Find the country with the highest CO2 emissions
# most_co2_emission_country = co2_emission_by_country.loc[co2_emission_by_country['co2_emission'].idxmax()]['country']

# # Create the histogram
# # Create the histogram
# plt.hist(rice_consumption['co2_emission'], bins=130)

# # Add the title, xlabel, ylabel
# plt.xlabel("CO2 Emission (kg CO2 eq/kg food)")
# plt.ylabel("Frequency")
# plt.title("CO2 Emission of Rice Consumption")

# # Get the highest CO2 emission value
# max_co2_emission = co2_emission_by_country.loc[co2_emission_by_country['co2_emission'].idxmax()]['co2_emission']


# # Add the most CO2 Emission Country
# plt.text(x = max_co2_emission, y = max(plt.yticks()[0])*0.9,
#     s = f"Country with highest CO2 emissions: {most_co2_emission_country}",
#     fontsize = 10, color = 'blue',
#     ha = 'center', va = 'center')
# plt.show()


# rice_consumption[["country","co2_emission"]].sort_values("co2_emission", ascending=False).to_json("co2_emission_of_rice_consumption_sorted.json", orient='index')


#####################################################################################################################################

# rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# rice_mean = statistics.mean(rice_consumption['co2_emission'])
# rice_median = statistics.median(rice_consumption['co2_emission'])

# df = pd.DataFrame(
#     {
#         "Mean" : [(rice_mean)], '| '
#         "Median" : [(rice_median)]
#     }
# )

# print(df)
# print()

# #####################################################################################################################################

# co2_emission = food_consumption['co2_emission']
# sorted_data = food_consumption.sort_values("co2_emission", ascending=False).to_json("Quantile_sample.json", orient='index') 

# print(sorted_data)

# x = np.quantile(co2_emission, np.linspace(0, 1, 6))
# # Quantile: bize veri gruplarinin belli bir orana bolunmesine ve bu oran grruplarinin en yuksek degerini vermesine yarar.

# print(x)
# print()

# #####################################################################################################################################

food_category = food_consumption['food_category']

# co2_var = food_consumption.groupby('food_category')['co2_emission'].var()
# # print(co2_var)
# co2_std = food_consumption.groupby('food_category')['co2_emission'].std()
# # print(co2_std)

# data = {'co2_var': co2_var,
#         'co2_std': co2_std}

# df = pd.DataFrame(data)
# print(df)
# print()

# df = food_consumption.groupby('food_category')['co2_emission'].agg(['var', 'std', 'max', 'min', 'mean', 'median', 'mad'])
# print(df)

# #####################################################################################################################################

co2_beef = food_consumption[food_consumption['food_category'] == 'beef']
plt.hist(co2_beef['co2_emission'], bins=30)
plt.show()
print()


# co2_beef = food_consumption[food_consumption['food_category'] == 'beef']
# co2_emissions = co2_beef['co2_emission']

# # Divide the emissions data into 4 quantiles
# co2_emissions_q = pd.qcut(co2_emissions, 30)

# # Use your custom labels
# labels = ['Q{}'.format(i) for i in range(1,31)]
# # plt.figure(figsize=(5,5))
# # plt.title("CO2 Emissions for Beef Consumption")
# # # Create a pie chart
# # plt.pie(co2_emissions_q.value_counts(), labels=labels, autopct='%1.1f%%')
# # plt.show()


# plt.figure(figsize=(5,5))
# plt.title("CO2 Emissions for Beef Consumption")

# plt.plot(labels, co2_emissions_q.value_counts(), marker='o', linestyle='--', color='b')

# # Create a line chart with emissions data on the y-axis and 
# # quantile labels on the x-axis
# plt.plot(labels, co2_emissions_q.value_counts())
# plt.xlabel('Quantile')
# plt.ylabel('Emissions')
# plt.show()