import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")

#delete the column index
data.drop(columns='index', inplace= True)

#print the information of data
print(data.info())

#Statistical summary about the dataset
print(data.describe())

#maximum duration of flight
print(data[data['duration']==49.830000])

#minimum duration of flight
print(data[data['duration']==0.830000])

#minmum price of flight
print(data[data['price']==12071.000000])