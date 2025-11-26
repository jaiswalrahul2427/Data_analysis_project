import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")

data.drop(columns='index', inplace= True)
print(data)