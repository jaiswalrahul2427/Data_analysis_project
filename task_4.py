#Does price varies with airlines.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=pd.read_csv("airlines_flights_data.csv")
print(data)

#grouping the airlines and check their mean price
data.groupby('airline')['price'].mean()

#Drawing a Categorical plot showing the mean ticket price for each Airline
sns.catplot(x='airline',y='price',kind='bar',palette='dark',data=data,hue='class')
plt.show()