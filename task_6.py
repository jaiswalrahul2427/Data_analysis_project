#How the price changes with change in source and destination.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")
print(data)

#checking the mean ticket price for each source city
print(data.groupby('source_city')['price'].mean())


#checking the mean ticket price for each destination city
print(data.groupby('source_city')['price'].mean())


g=sns.relplot(x='destination_city',y='price',data=data,col="source_city",kind='line')
g.set_xticklabels(rotation=45)
plt.show()


# g=sns.relplot(x='destination_city',y='price',data=data,col="source_city",kind='line')
# plt.show()

