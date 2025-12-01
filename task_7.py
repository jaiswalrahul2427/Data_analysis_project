#How is the price affected when tickets are bought in just 1 or 2days before departure.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=pd.read_csv("airlines_flights_data.csv")
print(data)

print(data['days_left'].unique())

print(data.groupby('days_left')['price'].mean())

sns.relplot(x="days_left",y='price',kind='line',data=data)
plt.show()