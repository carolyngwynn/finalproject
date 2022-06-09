### importing packages such as pandas, numpy, and matplotlib
import pandas as pd
import matplotlib as plt
import numpy as np

#importing data file for temperature change over the course of numerous years and countries, we will reference and call upon
#this data in the main script to then create functions and graph the data to further analayze.
file = pd.read_csv('/Users/carolyngwynn/Environment_Temperature_change_E_All_Data_NOFLAG 2.csv')

#extracting data from the imported file and assigning it to variables
country = file.loc[:, 'Area']
month = file.loc[:, 'Months']
year1 = file.loc [:, 'Y1961']
year2 = file.loc [:, 'Y1962']
year3 = file.loc [:, 'Y1963']
year4 = file.loc [:, 'Y1964']
year5 = file.loc [:, 'Y1965']
year6 = file.loc [:, 'Y1966']
year7 = file.loc [:, 'Y1967']
year8 = file.loc [:, 'Y1968']
year9 = file.loc [:, 'Y1969']
year10 = file.loc [:, 'Y1970']
num = 1
#position of the country in the data set
def position(country1):
    for i in range(len(country)):
        if str(country[i]) == country1:
            num = i
            break
    return num

# calculating the tempature change in 10 years for one country
def tempchange(country1):
    num = position(country1)
    change = year10[num] - year1[num]
    return change
# sorting the data set from least to greatest to determine what country has the smallest increase or decrease out of the 3
def sortarray(arrays):
    output = []
    output = np.sort(arrays)
    return output










