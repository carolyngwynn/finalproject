# Name: Carolyn Gwynn
# File name: Final project for Engineering 103
#Date : 6/07/22
# Description: This program calculates the temperature change for three countries in which you can choose which to compare
#on a graph and visually analyze the differences in data.
# Input: countries selected from data set list
#output: The temperature changes ( increase or decrease) of the three countries selected.
### importing packages such as pandas, numpy, and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import library as lb
# I is a counter and the while loop is used to limit the number of countries the user will input which is limited to 3
i = 0
output = []
while i < 3:
    country = input(" please select a country from the data list, make sure to capitalize the country.")
    change = lb.tempchange(country)
    print('the tempature change in ', country, 'was', change)
    output.append(change)
    i += 1
##printing the ouput as well as sorting the output so it is arranged from least to greatest and we can see all 3 countries
#data clearly
print(output)
print(lb.sortarray(output))
print('the tempature changed', )

### graphing the data of the 3 countries to illustrate the differences in temp changes and allowing us to analyze them in
#reference to eachother

x = np.arange(3)
y = output
fig,ax = plt.subplots()
plt.plot(x,y)
plt.show()



