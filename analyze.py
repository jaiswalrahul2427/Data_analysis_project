import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#The Flights Dataset
#Here,The flights Booking Dataset of various Airlines is a scarped datewise from
#a famous website in a structure format.The datset contains the records of fight travel details between the cities between the cities in india.
#Here,multiple features are present like Source & departure Time, Duration & Price of the flight etc.

#This data is availables as a CSV file.We are going to analyze this data set using the pandas DataFrame.
#This analyse will be helpful for those working in Airlines,Travel domain.






data = pd.read_csv("airlines_flights_data.csv")
print(data.head(5))
