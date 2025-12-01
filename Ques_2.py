import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("airlines_flights_data.csv")
data.drop(columns='index', inplace=True)

# Departure time counts
dep_counts = data['departure_time'].value_counts()
print(dep_counts)

# Arrival time counts
arr_counts = data['arrival_time'].value_counts()
print(arr_counts)

# Plotting
plt.figure(figsize=(16,4))

# ----- Departure Time -----
plt.subplot(1,2,1)
plt.bar(dep_counts.index, dep_counts.values)
plt.title("Departure Time Counts")
plt.xlabel("Departure Time")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

# ----- Arrival Time -----
plt.subplot(1,2,2)
plt.bar(arr_counts.index, arr_counts.values)
plt.title("Arrival Time Counts")
plt.xlabel("Arrival Time")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
