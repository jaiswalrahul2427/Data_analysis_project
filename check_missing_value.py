import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data=pd.read_csv('airlines_flights_data.csv')

#check for the missing values in any column
print(data.isnull().sum())
