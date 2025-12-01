import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")
print(data)
# Average price for each arrival time
print("Average Price by Arrival Time:")
# plt.figure(figsize=(8,5))
print(data.groupby('arrival_time')['price'].mean())
sns.catplot(x='arrival_time',y='price',kind='bar',data=data,col='airline',height=6,aspect=1)
plt.show()


# Average price for each departure time
print("\nAverage Price by Departure Time:")
print(data.groupby('departure_time')['price'].mean())
sns.catplot(x='arrival_time',y='price',kind='bar',data=data,height=6,aspect=1)
plt.show()
