import pandas as pd
import numpy as np

# This is coursera capstone project where using supervised learning we will learn about Collisions Severity
# I will use Jupyter notebooks as well as PyCharm and the reason is that Coursera asks me to use Jpuyter Notebooks when I need to practice PyCharm for my workplace.

print("Hello Capstone Project Course!")
data = pd.read_csv("C:/Users/fajlh/OneDrive/Documents/IBM_DS/Data-Collisions.csv", low_memory=False)

print(data.head())

print(data.columns)

print(data.dtypes)
# mixed datatype
# Goal: Predict Severity Code using SeverityCodeID
# It has unbalanced labels you need to balance data

print(data.shape[1])

print(data.isnull().sum())