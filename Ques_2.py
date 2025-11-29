#Show bar Graphs representing the departure time & Arrival time.

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("airlines_flights_data.csv")
data.drop(columns='index', inplace= True)

# print(data)

# data['departure_time'].value_counts()
# plt.xlabel("departure_time")
# plt.ylabel("arrival_time")
# plt.show()
departure_data=data['departure_time'].value_counts(ascending=True)
arrival_data=data['arrival_time'].value_counts(ascending=True)
 
plt.bar(departure_data.index,departure_data.values)
plt.show()
21.24