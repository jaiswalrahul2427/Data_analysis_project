#What are the airlines in the dataset,accompanied by their frequencies?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")
data.drop(columns='index', inplace= True)

#Number of Airline company in dataset
print(data['airline'].nunique())

#Name of Airline company in dataset
print(data['airline'].unique())

#Showing all the Airlines with their frequencies
print(data['airline'].value_counts())

#showing all the Airline with their number of flight in graph
data['airline'].value_counts(ascending=True).plot.barh(color=['lightgreen','lightblue'])
plt.xlabel("Airline")
plt.ylabel("Number of Flights")
plt.title("Number of Flights by Airline")
#plt.tight_layout() automatically adjusts the padding around the plot
plt.tight_layout()

plt.show()

