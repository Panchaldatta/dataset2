# 2. Write a python program to splitting the dataset into training and testing set. 

import pandas as pd
from sklearn.datasets import load_iris
iris_data=load_iris()
df=pd.DataFrame(iris_data.data)
print(df)
training_data=df.sample(frac=0.8,random_state=25)
testing_data=df.drop(training_data.index)
print(f"No of training examples: {training_data.shape[0]}")
print(f"No of testing examples: {testing_data.shape[0]}")
