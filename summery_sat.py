import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
#read the data
#./dataset/ is a path. Copy and paste the path of the CSV file in your computer to read the data. 
food_consumption = pd.read_csv('food_consumption.csv',index_col=0)

food_consumption.head(6)
# print(food_consumption.head(6))
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
# print(be_consumption)

# Q-1) Calculate mean and median consumption in Belgium

mean=be_consumption['consumption'].mean()
print(mean)
median=be_consumption['consumption'].median()
print(median)

# Q-2) Calculate mean and median consumption of USA

usa_consumption=food_consumption[food_consumption['country'] == 'USA']
# print(usa_consumption)
mean_usa=usa_consumption['consumption'].mean()
print(mean)
median_usa=usa_consumption['consumption'].median()
print(median_usa)

# Q-3) Group by country, select consumption column, and compute mean and median

usa_and_be=food_consumption[(food_consumption['country'] == 'Belgium')|(food_consumption['country'] == 'USA')]
print(usa_and_be)
t=usa_and_be.groupby('country')['consumption'].mean()
y=usa_and_be.groupby('country')['consumption'].median()
s=[t,y]

d=pd.concat(s,axis=1,join='inner',keys=["mean", "median"])
print(d)
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
print(rice_consumption)

# Q-4)Plot the histogram of co2_emission for rice

rice_consumption["co2_emission"].diff().hist()
pt.show () 

# Q-5) Calculate mean and median of co2_emission with .agg()
ag1=rice_consumption.agg((['mean', 'median']))
print(ag1)

print(rice_consumption["co2_emission"].mean())
print(rice_consumption["co2_emission"].median())



# Q-6) Calculate the quintiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 6)))

# Q-7) Calculate the variance and standard deviation of co2_emission 
# for food_categories

food_consumption = pd.read_csv('food_consumption.csv',index_col=0)
print(food_consumption)
beef_cat=food_consumption[food_consumption['food_category'] == 'beef']

# beef_cat["co2_emission"].diff().hist()
# pt.show () 

print(beef_cat)
print(beef_cat['co2_emission'].mean())
print(food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].median())

n=['beef','dairy', 'eggs' ,'fish','lamb_goat','nuts','pork','poultry','rice','soybeans','wheat'             
  ]
df1=[]
df2=[]
for i in n:
        
        # df1[i]=food_consumption[food_consumption['food_category'] == i]['co2_emission'].var()
         df1.append(food_consumption[food_consumption['food_category'] == i]['co2_emission'].var())
print(i,df1)
r1=pd.DataFrame(df1)
print(r1)
for i in n:
        
        # df2[i]=food_consumption[food_consumption['food_category'] == i]['co2_emission'].std()
        df2.append(food_consumption[food_consumption['food_category'] == i]['co2_emission'].std())
print(df2)
r2=pd.DataFrame(df2)
print(r2)
s={"food_category":n,"mean":df1,"std":df2}
s=pd.DataFrame(s)
print(s)

# Q-8) Create histogram of co2_emission for food_category 'beef'

beef_cat["co2_emission"].diff().hist()
pt.show () 




