import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)
 
food_consumption = pd.read_csv('./food_consumption.csv', index_col=0)
food_consumption.head()
    
#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
print(be_consumption.head())
# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

## Q-1) Calculate mean and median consumption in Belgium



