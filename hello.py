print("Hello")

import pandas as pd

data = pd.read_csv("C:/Users/fajlh/OneDrive/Documents/IBM_DS/Data-Collisions.csv", low_memory=False)

print(data.head())

print(data.columns)