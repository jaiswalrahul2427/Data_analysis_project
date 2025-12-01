#show Bar Graph representing the source City & Destination City
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=pd.read_csv("airlines_flights_data.csv")
print(data)

print(data['source_city'].value_counts())


#Graph representing the source City
plt.figure(figsize=(16,4))
plt.subplot(1,2,1)
plt.bar(data['source_city'].value_counts().index,data['source_city'].value_counts().values,color=["red","green"])
font=fontdict={'fontsize':12,'fontweight':'bold'}
plt.xlabel("Source City Name",fontdict={'fontsize':12,'fontweight':'bold'})
plt.ylabel("No of Flight",font)
plt.title("Graph representing the source City",font)
# plt.show()

#Graph representing the Destination City
print(data['destination_city'].value_counts())
plt.subplot(1,2,2)
plt.bar(data['destination_city'].value_counts().index,data['destination_city'].value_counts().values,color=["blue","gray"])
font=fontdict={'fontsize':12,'fontweight':'bold'}
plt.xlabel("Source City Name",fontdict={'fontsize':12,'fontweight':'bold'})
plt.ylabel("No of Flight",font)
plt.title("Graph representing the source City",font)

plt.tight_layout()
plt.show()
