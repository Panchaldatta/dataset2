# 1. Write a python program to find all null values in a given data set and remove them. 
# (Download dataset from github.com) 


import pandas as pd
dataset=pd.read_csv('city_day.csv')
dataset
dataset.isnull()
dataset.isnull().head(10)
dataset.isnull().sum()
dataset.isnull().head().sum()
modifieddataset=dataset.fillna(" ")
modifieddataset.isnull().sum()
dataset=dataset.dropna()
